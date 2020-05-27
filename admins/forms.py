from django import forms

from accounts.models import CustomUser
from .models import AdminProfile
from accounts.forms import UserUpdateForm


class AdminProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = AdminProfile
        fields = ['profile_pic', ]