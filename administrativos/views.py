from django.shortcuts import render
from django.views.generic import ListView
from usuarios.models import TuHogar360

# Create your views here.
class AdministrativosView(ListView):
   model = TuHogar360
   template_name = 'administrativos.html'
   context_object_name = 'list_usuarios'

   def get_queryset(self):
      return TuHogar360.objects.all()
    
