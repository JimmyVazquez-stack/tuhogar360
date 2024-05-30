import django_filters
from .models import Propiedad

class PropiedadFilter(django_filters.FilterSet):
    num_habitaciones = django_filters.RangeFilter()
    num_baños = django_filters.RangeFilter()
    num_estacionamientos = django_filters.RangeFilter()

    class Meta:
        model = Propiedad
        fields = ['num_habitaciones', 'num_baños', 'num_estacionamientos']