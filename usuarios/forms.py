from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
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
        model = CustomUser
        fields = [ 'username', 'first_name', 'last_name', 'email',]

    def __init__(self, *args, **kwargs):
        super(PerfilForm, self).__init__(*args, **kwargs)
        # Personaliza los widgets si es necesario
        self.fields['fecha_nacimiento'].widget.attrs.update({'class': 'datepicker'})  # Por ejemplo, puedes añadir una clase de datepicker para usar un selector de fecha

''' 
class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = ['curp', 'rfc', 'identificacion']  # Agrega 'user' al formulario

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Obtén el usuario de los argumentos de la función
        super().__init__(*args, **kwargs)
        self.user = user  # Guarda el usuario en el formulario

    def save(self, commit=True):
        vendedor = super().save(commit=False)
        vendedor.user = self.user
        if commit:
            vendedor.save()
        return vendedor
'''
    