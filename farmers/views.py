from django.views.generic import TemplateView


class FarmerHomeView(TemplateView):
    """Add Farmer Dashboard view """
    template_name = 'farmer/farmer_home.html'
