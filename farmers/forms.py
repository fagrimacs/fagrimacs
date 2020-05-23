from django import forms

from accounts.models import CustomUser
from farmers.models import FarmerProfile
from accounts.forms import UserUpdateForm


class FarmerProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = FarmerProfile
        fields = ['profile_pic', ]