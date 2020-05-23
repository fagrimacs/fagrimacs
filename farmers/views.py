from django.views.generic import TemplateView, DetailView, UpdateView
from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin
)
from django.contrib.messages.views import SuccessMessageMixin

from .models import FarmerProfile
from .forms import FarmerProfileUpdateForm, UserUpdateForm


class FarmerHomeView(TemplateView):
    """Add Farmer Dashboard view """
    template_name = 'farmers/farmer_home.html'


class FarmerProfileView(DetailView):
    model = FarmerProfile
    template_name = 'farmers/farmer_profile.html'
    context_object_name = 'farmer_profile'


class FarmerProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = FarmerProfile
    form_class = FarmerProfileUpdateForm
    success_message = "Your profile has been updated successful."

    def test_func(self):
        if self.request.user.farmerprofile == FarmerProfile.objects.get(user_id=self.kwargs['pk']):
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = UserUpdateForm
        context['profile_form'] = FarmerProfileUpdateForm
        return context