from django import forms

from accounts.models import CustomUser
from farmers.models import FarmerProfile


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['name', 'phone', ]


class FarmerProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = FarmerProfile
        fields = ['profile_pic', ]