from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView, LogoutView

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

class RegistroUsuarioView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registro.html" # Nombre de la template de registro
    
    def get_success_url(self):
        return reverse_lazy('ingreso') # Redirecciona al login despues del registro

class CustomLoginView(LoginView):
    template_name = "login.html"

    def get_success_url(self):
        user = self.request.user
        if user.is_superuser:
            return reverse_lazy('admin:index')
        else:
            return reverse_lazy('usuarios')
        
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('usuarios')

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        return response
    
class PerfilUsuarioView(TemplateView):
    template_name = 'perfil.html'