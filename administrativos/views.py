from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class AdministrativosView(TemplateView):
   template_name = "administrativos.html" 
    
