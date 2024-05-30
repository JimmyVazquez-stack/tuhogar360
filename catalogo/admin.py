from django.contrib import admin
from .models import Propiedad
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Sepomex
from django.core.management import call_command

class SepomexAdmin(admin.ModelAdmin):
    search_fields = ('d_codigo', 'd_asenta')  # Buscar por código postal y colonia
    # Define la función para la acción personalizada
    def cargar_datos(self, request, queryset):
        # Obtiene la ruta del archivo CSV (reemplaza 'ruta/a/tu/archivo.csv' con la ruta a tu archivo)
        csv_file = 'sepomex_db.csv'
        # Llama al comando de gestión personalizado con la ruta del archivo CSV
        call_command('load_data', csv_file)
    cargar_datos.short_description = "Cargar datos desde CSV"  # Nombre de la acción

    # Agrega la acción personalizada al admin
    actions = ['cargar_datos']

admin.site.register(Sepomex, SepomexAdmin)

class PropiedadAdmin(admin.ModelAdmin):
    list_display = ('fecha_publicacion','descripcion','direccion', 'usuario', 'precio', 'area', 'num_habitaciones', 'num_baños')
    search_fields = ('direccion', 'usuario__username')  # Buscar por dirección y nombre de usuario
    list_filter = ('usuario',)  # Filtrar por usuario

admin.site.register(Propiedad, PropiedadAdmin)