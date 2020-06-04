from django import forms

from . models import Implement


class ImplementForm(forms.ModelForm):

    class Meta:
        model = Implement
        exclude = ('user',)
        field = ('name','age',)