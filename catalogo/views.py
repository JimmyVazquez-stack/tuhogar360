from django.shortcuts import render
from django.views.generic import TemplateView

class DetallesCasaView(TemplateView):
    template_name = 'detalles.html'