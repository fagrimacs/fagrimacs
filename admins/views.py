from django.views.generic import TemplateView, DetailView, UpdateView
from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin
)
from django.contrib.messages.views import SuccessMessageMixin

from .models import AdminProfile
from .forms import AdminProfileUpdateForm
from accounts.forms import UserUpdateForm


class AdminHomeView(TemplateView):
    """Add Farmer Dashboard view """
    template_name = 'admin/admin_home.html'


class FarmersView(TemplateView):
    """Add Farmer List view """
    template_name = 'admin/farmers.html'


class OwnersView(TemplateView):
    """Add Owner List view """
    template_name = 'admin/owners.html'


class ProfileView(TemplateView):
    """Add Profile view """
    template_name = 'admin/admin_profile.html'
 

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