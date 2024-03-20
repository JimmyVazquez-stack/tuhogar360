from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Vista360(TemplateView):
    template_name = "vista360.html"