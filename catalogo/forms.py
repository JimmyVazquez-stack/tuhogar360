from .models import Propiedad
from django import forms

class PropiedadForm(forms.ModelForm):
    estado = forms.CharField(widget=forms.TextInput(attrs={'id': 'id_d_estado', 'name' : 'd_estado'}), max_length=100, required=False)
    ciudad = forms.CharField(widget=forms.TextInput(attrs={'id': 'id_d_ciudad', 'name' : 'd_ciudad'}), max_length=100, required=False)
    municipio = forms.CharField(widget=forms.TextInput(attrs={'id': 'id_D_mnpio', 'name' : 'D_mnpio'}), max_length=100, required=False)
    asentamiento = forms.CharField(widget=forms.TextInput(attrs={'id': 'id_d_asenta', 'name' : 'd_asenta'}), max_length=100, required=False)
    codigo_postal = forms.CharField(widget=forms.TextInput(attrs={'id': 'id_codigo_postal','name' : 'codigo_postal'}), max_length=5, required=False)
    area = forms.DecimalField(label='Area m²:',widget=forms.NumberInput(attrs={'step': '0.01'}), max_digits=10, decimal_places=2)
    num_habitaciones = forms.IntegerField(label='Habitaciones:', widget=forms.NumberInput(attrs={'min': '0'}))
    num_baños = forms.IntegerField(label='Baños:', widget=forms.NumberInput(attrs={'min': '0'}))
    num_estacionamientos = forms.IntegerField(label='Cajones de estacionamientos:', widget=forms.NumberInput(attrs={'min': '0'}))



    class Meta:
        model = Propiedad
        fields = ['precio', 'area', 'tipo_propiedad', 'num_habitaciones', 'num_baños', 'num_estacionamientos', 'imagen_principal', 'descripcion', 'estado','direccion', 'ciudad', 'asentamiento', 'municipio', 'codigo_postal', ]
        widgets = {
            'fecha_publicacion': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Pop 'user' del kwargs
        super(PropiedadForm, self).__init__(*args, **kwargs)
        self.user = user  # Guarda 'user' como un atributo del formulario
    

class PropiedadSEPOMEXForm(PropiedadForm):
    class Meta(PropiedadForm.Meta):
        fields = PropiedadForm.Meta.fields + ['codigo_postal']

    

class BusquedaForm(forms.Form):
    query = forms.CharField(label='', max_length=255, required=False, widget=forms.TextInput(attrs={'placeholder': 'Buscar...'}))
    num_habitaciones = forms.IntegerField(label='', required=False, widget=forms.NumberInput(attrs={'placeholder': 'Número de habitaciones'}))
    num_baños = forms.IntegerField(label='', required=False, widget=forms.NumberInput(attrs={'placeholder': 'Número de baños'}))
    num_estacionamientos = forms.IntegerField(label='', required=False, widget=forms.NumberInput(attrs={'placeholder': 'Número de estacionamientos'}))