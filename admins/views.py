from django.views.generic import TemplateView


class AdminHomeView(TemplateView):
    """Add Farmer Dashboard view """
    template_name = 'admin/admin_home.html'


class FarmersView(TemplateView):
    """Add Farmer List view """
    template_name = 'admin/farmers.html'


class OwnersView(TemplateView):
    """Add Owner List view """
    template_name = 'admin/owners.html'
