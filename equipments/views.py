from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from . forms import ImplementForm


class ImplementView(CreateView):
    form_class = ImplementForm
    template_name = 'equipments/implement_form.html'
    success_url = reverse_lazy('/')
    context_object_name = 'implement'
