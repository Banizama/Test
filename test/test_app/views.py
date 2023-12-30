from django.shortcuts import render
from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = 'home.html'

class Page1(TemplateView):
    template_name = 'page1.html'


class Page2(TemplateView):
    template_name = 'page2.html'
