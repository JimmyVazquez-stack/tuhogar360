# Generated by Django 5.0.6 on 2024-05-30 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0004_remove_propiedad_imagenes_360_propiedad_asentamiento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propiedad',
            name='fecha_publicacion',
            field=models.DateField(auto_now_add=True),
        ),
    ]
