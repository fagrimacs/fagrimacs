from django.views.generic import TemplateView, View, DetailView, UpdateView
from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin
)
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .models import FarmerProfile
from .forms import FarmerProfileUpdateForm, UserUpdateForm


class FarmerHomeView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    """View for showing Farmer Dashboard."""

    template_name = 'farmers/farmer_home.html'

    def test_func(self):
        if self.request.user.is_farmer:
            return True
        return False


class FarmerProfileView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """View for showing Farmer Profile."""
    model = FarmerProfile
    template_name = 'farmers/farmer_profile.html'
    context_object_name = 'farmer_profile'

    def test_func(self):
        if self.request.user.farmerprofile == FarmerProfile.objects.get(user_id=self.kwargs['pk']):
            return True
        return False


class FarmerProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, View):
    """View for updating farmers profile."""

    def get(self, request, pk):
        context = {
            'user_form': UserUpdateForm(instance=request.user),
            'profile_form': FarmerProfileUpdateForm(instance=request.user.farmerprofile)
        }
        return render(request, 'farmers/farmerprofile_form.html', context)

    def post(self, request, pk):
        if request.method == 'POST':
            user_form = UserUpdateForm(request.POST, instance=request.user)
            profile_form = FarmerProfileUpdateForm(request.POST, request.FILES, instance=request.user.farmerprofile)

            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.success(request, 'Your profile has been updated successful.')
                return redirect(reverse('farmers:farmer-profile', kwargs={'pk': request.user.pk}))
        else:
            user_form = UserUpdateForm(instance=request.user)
            profile_form = FarmerProfileUpdateForm(instance=request.user.farmerprofile)

    def test_func(self):
        if self.request.user.farmerprofile == FarmerProfile.objects.get(user_id=self.kwargs['pk']):
            return True
        return False