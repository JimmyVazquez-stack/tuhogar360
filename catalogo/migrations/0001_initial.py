# Generated by Django 5.0.6 on 2024-05-28 04:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen360',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='propiedades/360')),
            ],
        ),
        migrations.CreateModel(
            name='Propiedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('descripcion', models.TextField()),
                ('direccion', models.CharField(max_length=255)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('area', models.DecimalField(decimal_places=2, max_digits=10)),
                ('num_habitaciones', models.PositiveIntegerField()),
                ('num_baños', models.PositiveIntegerField()),
                ('imagen_principal', models.ImageField(upload_to='propiedades')),
                ('imagenes_360', models.ManyToManyField(blank=True, to='catalogo.imagen360')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='propiedades', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
