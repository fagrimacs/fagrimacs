from django.views.generic import TemplateView, View, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import render, redirect, reverse

from owners.models import OwnerProfile
from .forms import OwnerProfileUpdateForm
from accounts.forms import UserUpdateForm


class OwnerHomeView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    """View to show Farmer Dashboard."""
    template_name = 'owners/owner_home.html'

    def test_func(self):
        if self.request.user.is_owner:
            return True
        return False


class OwnerProfileView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """View for showing Owner profile."""
    model = OwnerProfile
    template_name = 'owners/owner_profile.html'
    context_object_name = 'owner_profile'

    def test_func(self):
        if self.request.user.ownerprofile == OwnerProfile.objects.get(user_id=self.kwargs['pk']):
            return True
        return False


class OwnerProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, View):
    """View for updating onwers profile."""

    def get(self, request, pk):
        context = {
            'user_form': UserUpdateForm(instance=request.user),
            'profile_form': OwnerProfileUpdateForm(instance=request.user.ownerprofile)
        }
        return render(request, 'farmers/farmerprofile_form.html', context)

    def post(self, request, pk):
        if request.method == 'POST':
            user_form = UserUpdateForm(request.POST, instance=request.user)
            profile_form = OwnerProfileUpdateForm(request.POST, request.FILES, instance=request.user.ownerprofile)

            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.success(request, 'Your profile has been updated successful.')
                return redirect(reverse('owners:owner-profile', kwargs={'pk': request.user.pk}))
        else:
            user_form = UserUpdateForm(instance=request.user)
            profile_form = OwnerProfileUpdateForm(instance=request.user.ownerprofile)

    def test_func(self):
        if self.request.user.ownerprofile == OwnerProfile.objects.get(user_id=self.kwargs['pk']):
            return True
        return False