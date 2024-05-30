from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView
from .models import Propiedad  # Import the Propiedad model
from django.views.generic import ListView, CreateView
from usuarios.models import CustomUser
from .forms import PropiedadForm   # Import the PropiedadForm form
from django.urls import reverse
from usuarios.permissions import verificar_limite_publicaciones
from django.core.exceptions import PermissionDenied
import logging
from django.db.models import Q
from .forms import BusquedaForm
from .models import Sepomex
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect


class AnunciosView(ListView):
    model = Propiedad
    template_name = 'anuncios.html'
    context_object_name = 'propiedades'
    paginate_by = 6  # Número de propiedades por página

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(validado=True)
        form = BusquedaForm(self.request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('query')
            num_habitaciones = form.cleaned_data.get('num_habitaciones')
            num_baños = form.cleaned_data.get('num_baños')
            num_estacionamientos = form.cleaned_data.get('num_estacionamientos')
            if query:
                queryset = queryset.filter(
                    Q(direccion__icontains=query) | Q(descripcion__icontains=query )| Q(estado__icontains=query )| Q(codigo_postal__icontains=query )
                )
            if num_habitaciones is not None:
                queryset = queryset.filter(num_habitaciones=num_habitaciones)
            if num_baños is not None:
                queryset = queryset.filter(num_baños=num_baños)
            if num_estacionamientos is not None:
                queryset = queryset.filter(num_estacionamientos=num_estacionamientos)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BusquedaForm(self.request.GET)
        return context

class DetallesCasaView(DetailView):
    model = Propiedad
    template_name = 'detalles_propiedad_usuario.html'
    context_object_name = 'propiedad'
    pk_url_kwarg = 'propiedad_id'

class DetallesCasaTodosView(DetailView):
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
    paginate_by = 3


    def post(self, request, *args, **kwargs):
        propiedad_id = request.POST.get('id')
        propiedad = get_object_or_404(Propiedad, id=propiedad_id)
        if propiedad.usuario == request.user:
            propiedad.delete()
        return HttpResponseRedirect(reverse('mis_publicaciones', kwargs={'username': request.user.username}))

    def get_queryset(self):
        # Obtenemos el usuario actual
        usuario = self.request.user
        # Filtramos las propiedades relacionadas con el usuario actual
        queryset = Propiedad.objects.filter(usuario=usuario)
        # Obtenemos el término de búsqueda
        query = self.request.GET.get('query')
        if query:
            # Filtramos las propiedades que coinciden con el término de búsqueda en nombre o descripción
            queryset = queryset.filter(
                Q(direccion__icontains=query) | Q(descripcion__icontains=query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BusquedaForm(self.request.GET)
        return context
    

    
logger = logging.getLogger(__name__)   



class NuevaPublicacion(LoginRequiredMixin, CreateView):
    model = Propiedad
    form_class = PropiedadForm
    template_name = 'nueva_publicacion.html'
    success_url = '/catalogos/mis_publicaciones/{{ request.user.username }}'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        try:
            verificar_limite_publicaciones(self.request.user)
        except PermissionDenied as e:
            logger.error(f"Permission denied: {e}")
            form.add_error(None, str(e))
            return self.form_invalid(form)
        
        if self.request.POST.get('llenar_datos_sepomex'):
            codigo_postal = self.request.POST.get('codigo_postal')
            if codigo_postal:
                datos_sepomex = consulta_sepomex(codigo_postal)
                if datos_sepomex:
                    form.instance.estado = datos_sepomex.get('d_estado', '')
                    form.instance.ciudad = datos_sepomex.get('d_ciudad', '')
                    form.instance.municipio = datos_sepomex.get('D_mnpio', '')
                    form.instance.asentamiento = datos_sepomex.get('d_asenta', '')
                    form.instance.codigo_postal = datos_sepomex.get('codigo_postal', '')
                    # Llena otros campos según sea necesario

        response = super().form_valid(form)
        logger.info(f"Propiedad publicada por {self.request.user.username}")
        return response
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['codigo_postal'] = self.request.POST.get('codigo_postal')  # Obtener el código postal del POST
        return context

    
def consulta_sepomex(request):
    d_codigo = request.GET.get('d_codigo', None)
    if d_codigo:
        sepomex = Sepomex.objects.filter(d_codigo=d_codigo).first()
        if sepomex:
            return JsonResponse({
                'd_estado': sepomex.d_estado,
                'd_ciudad': sepomex.d_ciudad,
                'D_mnpio': sepomex.D_mnpio,
                'd_asenta': sepomex.d_asenta,
                # Agrega más campos según sea necesario
            })
    return JsonResponse({'error': 'Código postal no encontrado'}, status=404)