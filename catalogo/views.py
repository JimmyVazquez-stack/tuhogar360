from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView
from .models import Propiedad  # Import the Propiedad model
from django.views.generic import ListView, CreateView
from usuarios.models import CustomUser
from .forms import PropiedadForm   # Import the PropiedadForm form

class AnunciosView(ListView):
    model = Propiedad
    template_name = 'anuncios.html'
    context_object_name = 'propiedades'
    paginate_by = 6  # Número de propiedades por página
    def get_queryset(self):
        return Propiedad.objects.all().order_by('-fecha_publicacion')  # Ordena las propiedades por fecha de publicación descendente

class DetallesCasaView(DetailView):
    model = Propiedad
    template_name = 'detalles.html'
    context_object_name = 'propiedad'
    pk_url_kwarg = 'propiedad_id'

class Vista360View(TemplateView):
    template_name = 'vista360.html'

class MisPublicacionesView(ListView):
    model = Propiedad
    template_name = 'mispublicaciones.html'
    context_object_name = 'propiedades'

    def get_queryset(self):
        # Obtenemos el nombre de usuario del usuario actual
        username = self.request.user.username
        # Obtenemos el objeto TuHogar360 del usuario actual
        usuario = CustomUser.objects.get(username=username)
        # Filtramos las propiedades relacionadas con el usuario actual
        return Propiedad.objects.filter(usuario=usuario)
    
    
class NuevaPublicacion(LoginRequiredMixin, CreateView):
    model = Propiedad
    form_class = PropiedadForm
    template_name = 'nueva_publicacion.html'
    success_url = '/catalogos/mis_publicaciones/{{ request.user.username }}'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs