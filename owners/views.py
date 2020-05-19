from django.views.generic import TemplateView


class OwnerHomeView(TemplateView):
    """Add Farmer Dashboard view """
    template_name = 'owner/owner_home.html'
