from django.test import TestCase
from django.urls import reverse

from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from accounts.models import CustomUser
from accounts.tokens import account_activation_token


class TestAccountsViews(TestCase):

    def test_user_login_view(self):
        response = self.client.get('/accounts/login/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')


    def test_user_logout_view(self):
        response = self.client.get('/accounts/logout/')

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')


    def test_user_signup_view(self):
        response = self.client.get(reverse('accounts:signup'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')


    def test_farmer_signup_view_GET(self):
        response = self.client.get(reverse('accounts:farmer-signup'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/farmer_signup.html')


    def test_farmer_signup_view_POST(self):
        signup_url = reverse('accounts:farmer-signup')
        response = self.client.post(signup_url, data={
            'email': 'test@farmer.com',
        })

        self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(response, 'registration/registration_pending.html')


    def test_confirm_registration_view_GET(self):
        self.user = CustomUser.objects.create_user(email='user@test.com', name='test-user')
        
        response = self.client.get(reverse('accounts:confirm-email', kwargs={
            'user_id': urlsafe_base64_encode(force_bytes(self.user.id)),
            'token': account_activation_token.make_token(self.user),
        }))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/registration_complete.html')


class TestSuccessUrlOnLogin(TestCase):
    """Test a success url for each user type when logged in."""

    def setUp(self):
        self.farmer_user = CustomUser.objects.create(
            name='Innocent', email='farmer@fagrimacs.com', is_farmer=True,
            password='idfsoiudiudf',
        )

    def test_farmer_success_url(self):
        response = self.client.login(email='farmer@fagrimacs.com', password='idfsoiudiudf')

        # self.assertTrue(response)