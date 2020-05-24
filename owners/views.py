from django.views.generic import TemplateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin

from owners.models import OwnerProfile
from .forms import OwnerProfileUpdateForm


class OwnerHomeView(TemplateView):
    """Add Farmer Dashboard view """
    template_name = 'owners/owner_home.html'


class OwnerProfileView(DetailView):
    model = OwnerProfile
    template_name = 'owners/owner_profile.html'
    context_object_name = 'owner_profile'


class OwnerProfileUpdateView(SuccessMessageMixin, UpdateView):
    model = OwnerProfile
    form_class = OwnerProfileUpdateForm
    success_message = "Your profile has been updated successful."