from django.views.generic import TemplateView


class AdminHomeView(TemplateView):
    """Add Farmer Dashboard view """
    template_name = 'admin/admin_home.html'
