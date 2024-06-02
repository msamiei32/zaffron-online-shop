from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.


class HomeClass(TemplateView):
    template_name = 'Home/home-classic.html'
