from django.shortcuts import render
from django.views.generic import TemplateView


class ComingSoonView(TemplateView):
    template_name = 'coming-soon.html'
