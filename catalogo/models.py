from django.db import models
from usuarios.models import CustomUser

class Propiedad(models.Model):
    TIPO_PROPIEDAD_CHOICES = [
        ('Terreno', 'Terreno'),
        ('Casa', 'Casa'),
        ('Departamento', 'Departamento'),
    ]

    usuario = models.ForeignKey(CustomUser, related_name='propiedades', on_delete=models.CASCADE)
    direccion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    num_habitaciones = models.IntegerField()
    num_baños = models.IntegerField()
    num_estacionamientos = models.IntegerField( default=0)
    imagen_principal = models.ImageField(upload_to='propiedades/')
    descripcion = models.TextField()
    fecha_publicacion = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=100, blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    municipio = models.CharField(max_length=100, blank=True, null=True)
    asentamiento = models.CharField(max_length=100, blank=True, null=True)
    codigo_postal = models.CharField(max_length=5, blank=True, null=True)
    validado = models.BooleanField(default=False)
    tipo_propiedad = models.CharField(max_length=20, choices=TIPO_PROPIEDAD_CHOICES, default='CA')

    def __str__(self):
        return self.direccion


class Imagen360(models.Model):
    imagen = models.ImageField(upload_to='propiedades/360')
    imagen = models.ImageField(upload_to='propiedades/360')

    def __str__(self):
        return f"Imagen 360 de la propiedad"

class Sepomex(models.Model):
    d_codigo = models.CharField(max_length=5)  # Código Postal
    d_asenta = models.CharField(max_length=100)  # Asentamiento (Colonia)
    d_tipo_asenta = models.CharField(max_length=100)  # Tipo de Asentamiento
    D_mnpio = models.CharField(max_length=100)  # Municipio
    d_estado = models.CharField(max_length=100)  # Estado
    d_ciudad = models.CharField(max_length=100)  # Ciudad
    d_CP = models.CharField(max_length=5)  # Código Postal
    c_estado = models.CharField(max_length=2)  # Clave de Estado
    c_oficina = models.CharField(max_length=5)  # Clave de Oficina
    c_CP = models.CharField(max_length=1)  # Clave de Código Postal
    c_tipo_asenta = models.CharField(max_length=2)  # Clave de Tipo de Asentamiento
    c_mnpio = models.CharField(max_length=4)  # Clave de Municipio
    id_asenta_cpcons = models.CharField(max_length=4)  # Identificador único de la colonia
    d_zona = models.CharField(max_length=50)  # Zona
    c_cve_ciudad = models.CharField(max_length=4)  # Clave de Ciudad

    def __str__(self):
        return f"{self.d_codigo} - {self.d_asenta}, {self.D_mnpio}, {self.d_estado}"