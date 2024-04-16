# usuarios/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class TuHogar360(AbstractUser):
    # Campos adicionales
    fecha_nacimiento = models.DateField(null=True, blank=True)
    is_usuarioTuHogar360 = models.BooleanField(default=True)
    telefono = models.CharField(max_length=15, blank=True)
    direccion = models.CharField(max_length=255, blank=True)
    imagen_perfil = models.ImageField(upload_to='imagenes_perfil', null=True, blank=True)
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    # Agrega otros campos según tus necesidades

    def __str__(self):
        return self.username


class Vendedor(models.Model):
    user = models.OneToOneField(TuHogar360, on_delete=models.CASCADE)  # Relación uno a uno con el modelo de usuario
    is_vendedorTuHogar360 = models.BooleanField(default=False)  # Campo para identificar que es un vendedor
    is_validando = models.BooleanField(default=True)  # Campo para validar si el vendedor ha sido validado
    curp = models.CharField(max_length=18)  # Campo para el CURP del vendedor
    rfc = models.CharField(max_length=13)  # Campo para el RFC del vendedor
    identificacion = models.FileField(upload_to='identificaciones/')  # Campo para cargar el archivo de identificación

    def __str__(self):
        return self.user.username
