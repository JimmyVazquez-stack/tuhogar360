from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Propiedad  # Import the Propiedad model
from django.views.generic import ListView
from usuarios.models import TuHogar360


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
        usuario = TuHogar360.objects.get(username=username)
        # Filtramos las propiedades relacionadas con el usuario actual
        return Propiedad.objects.filter(usuario=usuario)