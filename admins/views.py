import csv
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import render, reverse
from django.template.loader import get_template
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views.generic import TemplateView, DetailView, UpdateView, ListView
from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin
)
from django.contrib.messages.views import SuccessMessageMixin

from .models import AdminProfile
from .forms import AdminProfileUpdateForm
from accounts.forms import UserUpdateForm, FarmerSignUpForm, OwnerSignUpForm
from farmers.models import FarmerProfile
from owners.models import OwnerProfile
from accounts.tokens import account_activation_token
from accounts.models import CustomUser

class AdminHomeView(TemplateView):
    """Admin Dashboard view """
    template_name = 'admin/admin_home.html'
 

class AdminProfileView(DetailView):
    model = AdminProfile
    template_name = 'admin/admin_profile.html'
    context_object_name = 'admin_profile'


class AdminProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = AdminProfile
    form_class = AdminProfileUpdateForm
    template_name = 'admin/adminprofile_update.html'
    success_message = "Your profile has been updated successful."

    def test_func(self):
        if self.request.user.adminprofile == AdminProfile.objects.get(user_id=self.kwargs['pk']):
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = UserUpdateForm(instance=self.request.user)
        context['profile_form'] = AdminProfileUpdateForm(instance=self.request.user.adminprofile)
        return context

def register_farmer(request):
    """View for Admin to register farmer"""
    form = FarmerSignUpForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        user.email = form.cleaned_data['email']
        user.save()
        # Create profile
        farmer_profile = FarmerProfile(user=user)
        farmer_profile.save()
        # send confirmation email
        token = account_activation_token.make_token(user)
        user_id = urlsafe_base64_encode(force_bytes(user.id))
        url = 'http://fagrimacs.com' + reverse('accounts:confirm-email', kwargs={'user_id': user_id, 'token': token})
        message = get_template('registration/account_activation_email.html').render({
            'confirm_url': url
        })
        mail = EmailMessage('Fagrimacs Account Confirmation', message, to=[user.email], from_email=settings.EMAIL_HOST_USER)
        mail.content_subtype = 'html'
        mail.send()

        return render(request, 'admin/registration_pending.html',{
            'message': f'A confirmation email has been sent to your email. Please confirm to finish registration.'
            })
    return render(request, 'admin/register_farmer.html', {
        'form': form,
    })


def register_owner(request):
    """View for Admin to register farmer"""
    form = OwnerSignUpForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        user.email = form.cleaned_data['email']
        user.save()
        # Create profile
        owner_profile = OwnerProfile(user=user)
        owner_profile.save()
        # send confirmation email
        token = account_activation_token.make_token(user)
        user_id = urlsafe_base64_encode(force_bytes(user.id))
        url = 'http://fagrimacs.com' + reverse('accounts:confirm-email', kwargs={'user_id': user_id, 'token': token})
        message = get_template('registration/account_activation_email.html').render({
            'confirm_url': url
        })
        mail = EmailMessage('Fagrimacs Account Confirmation', message, to=[user.email], from_email=settings.EMAIL_HOST_USER)
        mail.content_subtype = 'html'
        mail.send()

        return render(request, 'admin/registration_pending.html',{
            'message': f'A confirmation email has been sent to your email. Please confirm to finish registration.'
            })
    return render(request, 'admin/register_owner.html', {
        'form': form,
    })


class FarmersListView(LoginRequiredMixin,UserPassesTestMixin, ListView):
    model = CustomUser
    template_name = 'admin/farmers.html'
    context_object_name = 'farmers'
    # paginate_by = 30
    queryset = CustomUser.objects.filter(is_farmer=True)

    def test_func(self):
        if self.request.user.is_admin:
            return True
        return False


class OwnersListView(LoginRequiredMixin,UserPassesTestMixin, ListView):
    model = CustomUser
    template_name = 'admin/owners.html'
    context_object_name = 'owners'
    queryset = CustomUser.objects.filter(is_owner=True)

    def test_func(self):
        if self.request.user.is_admin:
            return True
        return False


def export_farmers_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="farmers-list.csv"'

    writer = csv.writer(response)
    writer.writerow(['name','company','email','phone','country',])

    orders = CustomUser.objects.filter(is_farmer=True).values_list('name','company','email','phone','country',)
    for order in orders:
        writer.writerow(order)

    return response


def export_owners_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="owners-list.csv"'

    writer = csv.writer(response)
    writer.writerow(['name','company','email','phone','country',])

    orders = CustomUser.objects.filter(is_owner=True).values_list('name','company','email','phone','country',)
    for order in orders:
        writer.writerow(order)

    return response