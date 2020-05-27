from django.views.generic import TemplateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin

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


class OwnerProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = OwnerProfile
    form_class = OwnerProfileUpdateForm
    success_message = "Your profile has been updated successful."

    def test_func(self):
        if self.request.user.ownerprofile == OwnerProfile.objects.get(user_id=self.kwargs['pk']):
            return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = UserUpdateForm(instance=self.request.user)
        context['profile_form'] = OwnerProfileUpdateForm(instance=self.request.user.ownerprofile)
        return context
