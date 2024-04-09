from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import TuHogar360

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = TuHogar360
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    correo = forms.EmailField(label='Correo Electrónico')
    contrasena = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
# usuarios/forms.py
class RegistroForm(forms.Form):
    nombre_completo = forms.CharField(label='Nombre completo')
    correo = forms.EmailField(label='Correo Electrónico')
    usuario = forms.CharField(label='Usuario')
    contrasena = forms.CharField(widget=forms.PasswordInput, label='Contraseña')


class PerfilForm(forms.ModelForm):
    class Meta:
        model = TuHogar360
        fields = ['imagen_perfil', 'username', 'first_name', 'last_name', 'direccion', 'email', 'fecha_nacimiento', 'sexo']

    def __init__(self, *args, **kwargs):
        super(PerfilForm, self).__init__(*args, **kwargs)
        # Personaliza los widgets si es necesario
        self.fields['fecha_nacimiento'].widget.attrs.update({'class': 'datepicker'})  # Por ejemplo, puedes añadir una clase de datepicker para usar un selector de fecha