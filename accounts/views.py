from django.shortcuts import render, reverse
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from accounts.models import CustomUser

from accounts.forms import FarmerSignUpForm
from farmers.models import FarmerProfile
from accounts.tokens import account_activation_token
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.conf import settings


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


def farmer_signup(request):
    """Allow farmer to signup and activate their account"""
    form = FarmerSignUpForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        user.email = form.cleaned_data['email']
        user.save()
        # Create profile
        farmer_profile = FarmerProfile(user=user)
        farmer_profile.save()
        # send confirmation email
        token = account_activation_token.make_token(user)
        user_id = urlsafe_base64_encode(force_bytes(user.id))
        url = 'http://fagrimacs.com' + reverse('accounts:confirm-email', kwargs={'user_id': user_id, 'token': token})
        message = get_template('registration/account_activation_email.html').render({
            'confirm_url': url
        })
        mail = EmailMessage('Fagrimacs Account Confirmation', message, to=[user.email], from_email=settings.EMAIL_HOST_USER)
        mail.content_subtype = 'html'
        mail.send()

        return render(request, 'registration/registration_pending.html',{
            'message': f'A confirmation email has been sent to your email. Please confirm to finish registration.'
            })
    return render(request, 'registration/farmer_signup.html', {
        'form': form,
    })


class ConfirmRegistrationView(TemplateView):
    def get(self, request, user_id, token):
        user_id = force_text(urlsafe_base64_decode(user_id))

        user = CustomUser.objects.get(pk=user_id)

        context = {
            'message': 'Registration confirmation error. Please click the reset password to generate a new confirmation email.'
        }

        if user and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            context['message'] = 'Registration complete. Please login'

        return render(request, 'registration/registration_complete.html', context)
