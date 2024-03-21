from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UsuarioPersonalizado

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = UsuarioPersonalizado
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
