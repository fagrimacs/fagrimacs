from django.views.generic import TemplateView, DetailView, UpdateView
from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin
)
from django.contrib.messages.views import SuccessMessageMixin

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


class FarmerProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    """View for showing update view for farmer profile."""
    model = FarmerProfile
    form_class = FarmerProfileUpdateForm
    success_message = "Your profile has been updated successful."

    def test_func(self):
        if self.request.user.farmerprofile == FarmerProfile.objects.get(user_id=self.kwargs['pk']):
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = UserUpdateForm(instance=self.request.user)
        context['profile_form'] = FarmerProfileUpdateForm(instance=self.request.user.farmerprofile)
        return context