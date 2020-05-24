from django import forms

from accounts.models import CustomUser
from owners.models import OwnerProfile


class OwnerProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = OwnerProfile
        fields = ['profile_pic', ]