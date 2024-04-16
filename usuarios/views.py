from django.http.response import HttpResponse as HttpResponse
from .forms import CustomUserCreationForm, PerfilForm, VendedorForm
from .models import TuHogar360
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from catalogo.models import Propiedad

# Create your views here.
class UsuariosView(ListView):
    model = Propiedad
    template_name = "inicio.html"
    context_object_name = "propiedades"
    paginate_by = 3

    def get_queryset(self):
        return Propiedad.objects.all().order_by('-fecha_publicacion')
    

class NosotrosView(TemplateView):
    template_name = "nosotros.html"


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
            return reverse_lazy('usuarios')
        else:
            return reverse_lazy('usuarios')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('usuarios')

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        return response


class PerfilUsuarioView(LoginRequiredMixin, DetailView):
    model = TuHogar360
    template_name = 'perfil.html'
    context_object_name = 'perfil'

    def get_object(self, queryset=None):
        return self.request.user

    
class PerfilUpdateView(LoginRequiredMixin, UpdateView):
    model = TuHogar360
    form_class = PerfilForm
    template_name = 'editar_perfil.html'
    success_url = reverse_lazy('perfil')

    def get_object(self, queryset=None):
        return self.request.user
    

class VendedorFormView(LoginRequiredMixin,CreateView):
    model = TuHogar360
    form_class = VendedorForm
    template_name = 'vendedores_form.html'
    success_url = reverse_lazy('usuarios')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs