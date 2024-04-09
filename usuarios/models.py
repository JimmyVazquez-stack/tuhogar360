# usuarios/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class TuHogar360(AbstractUser):
    # Campos adicionales
    fecha_nacimiento = models.DateField(null=True, blank=True)
    is_vendedorTuHogar360 = models.BooleanField(default=False)
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
