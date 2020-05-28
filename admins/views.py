import csv
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import update_session_auth_hash
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import render, reverse, redirect
from django.template.loader import get_template
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views.generic import TemplateView, View, DetailView, UpdateView, ListView
from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin
)
from django.contrib.messages.views import SuccessMessageMixin

from .models import AdminProfile
from .forms import AdminProfileUpdateForm
from accounts.forms import UserUpdateForm, FarmerSignUpForm, OwnerSignUpForm
from farmers.models import FarmerProfile
from farmers.forms import FarmerProfileUpdateForm
from owners.models import OwnerProfile
from accounts.tokens import account_activation_token
from accounts.models import CustomUser

class AdminHomeView(TemplateView):
    """Admin Dashboard view """
    template_name = 'admin/admin_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['farmers'] = CustomUser.objects.filter(is_farmer=True)
        context['owners'] = CustomUser.objects.filter(is_owner=True)
        return context
        

class AdminProfileView(DetailView):
    model = AdminProfile
    template_name = 'admin/admin_profile.html'
    context_object_name = 'admin_profile'


class AdminProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, View):

    def get(self, request, pk):
        form = UserUpdateForm(instance=request.user)
        profile_form = AdminProfileUpdateForm(instance=request.user.adminprofile)
        context = {
                'form': form,
                'profile_form': profile_form
            }
        return render(request, 'admin/adminprofile_update.html', context)


    def post(self, request, pk):
        form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = AdminProfileUpdateForm(request.POST, request.FILES, instance=request.user.adminprofile)

        if form.is_valid() and profile_form.is_valid():
            form = form.save()
            custom_form = profile_form.save(False)
            custom_form.user = form
            custom_form.save()
            return redirect(reverse('admins:admin-homepage'))
            context = {
                'form': form,
                'profile_form': profile_form
            }
        return render(request, 'admin/adminprofile_update.html', context)
    
    def test_func(self):
        if self.request.user.adminprofile == AdminProfile.objects.get(user_id=self.kwargs['pk']):
            return True
        return False


class RegisterFarmerView(LoginRequiredMixin, UserPassesTestMixin, View):
    """View for Admin to register Farmer."""

    def get(self, request):
        return render(request, 'admin/register_farmer.html', {
            'form': FarmerSignUpForm(),
        })

    def post(self, request):
        if request.method == 'POST':
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
            else:
                return render(request, 'admin/register_farmer.html', {
                    'form': form,
                })
    
    def test_func(self):
        if self.request.user.is_admin:
            return True
        return False


class RegisterOwnerView(LoginRequiredMixin, UserPassesTestMixin, View):
    """View for Admin to register farmer"""

    def get(self, request):
        return render(request, 'admin/register_owner.html', {
            'form': OwnerSignUpForm(),
        })

    def post(self, request):
        if request.method == 'POST':
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
            else:
                return render(request, 'admin/register_owner.html', {
                    'form': form,
                })

    
    def test_func(self):
        if self.request.user.is_admin:
            return True
        return False


class FarmersListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = CustomUser
    template_name = 'admin/farmers.html'
    context_object_name = 'farmers'
    queryset = CustomUser.objects.filter(is_farmer=True)

    def test_func(self):
        if self.request.user.is_admin:
            return True
        return False


class OwnersListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = CustomUser
    template_name = 'admin/owners.html'
    context_object_name = 'owners'
    queryset = CustomUser.objects.filter(is_owner=True)

    def test_func(self):
        if self.request.user.is_admin:
            return True
        return False


class ExportFarmersCsv(LoginRequiredMixin, UserPassesTestMixin, View):
    """View for exporting Farmers list."""

    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="farmers-list.csv"'

        writer = csv.writer(response)
        writer.writerow(['name','company','email','phone','country',])

        orders = CustomUser.objects.filter(is_farmer=True).values_list('name','company','email','phone','country',)
        for order in orders:
            writer.writerow(order)

        return response
    
    def test_func(self):
        if self.request.user.is_admin:
            return True
        return False


class ExportOwnersCsv(LoginRequiredMixin, UserPassesTestMixin, View):
    """View for exporting Owners list."""

    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="owners-list.csv"'

        writer = csv.writer(response)
        writer.writerow(['name','company','email','phone','country',])

        orders = CustomUser.objects.filter(is_owner=True).values_list('name','company','email','phone','country',)
        for order in orders:
            writer.writerow(order)

        return response
    
    def test_func(self):
        if self.request.user.is_admin:
            return True
        return False