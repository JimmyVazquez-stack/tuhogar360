from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class UsuariosView(TemplateView):
    template_name = "inicio.html"

class NosotrosView(TemplateView):
    template_name = "nosotros.html"

class AnunciosView(TemplateView):
    template_name = "anuncios.html"

class BlogView(TemplateView):
    template_name = "blog.html"

class ContactoView(TemplateView):
    template_name = "contacto.html"

class RegistroView(TemplateView):
    template_name = "login.html"