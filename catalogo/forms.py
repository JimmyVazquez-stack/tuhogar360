from .models import Propiedad
from django import forms

class PropiedadForm(forms.ModelForm):
    class Meta:
        model = Propiedad
        fields = ['usuario', 'direccion', 'precio', 'area', 'num_habitaciones', 'num_baños', 'imagen_principal', 'imagen_principal', 'descripcion']
        widgets = {
            'fecha_publicacion': forms.DateInput(attrs={'type': 'date'}),
        }