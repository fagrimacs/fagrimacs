from django.shortcuts import render, reverse
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView


class UserLoginView(LoginView):
    """Allow user to login in platform """
    template_name = 'registration/login.html'

    def get_success_url(self):
        url = self.get_redirect_url()
        if url:
            return url
        elif self.request.user.is_farmer:
            return reverse('farmers:farmer-homepage')
        elif self.request.user.is_owner:
            return reverse('owners:owner-homepage')
        elif self.request.user.is_admin:
            return reverse('admins:admin-homepage')
        else:
            return f'/admin/'


class SignUpView(TemplateView):
    """Allow farmer and owner to signup"""
    template_name = 'registration/signup.html'
