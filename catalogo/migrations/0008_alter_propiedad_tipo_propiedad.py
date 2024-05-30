# Generated by Django 5.0.6 on 2024-05-30 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0007_propiedad_num_estacionamientos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propiedad',
            name='tipo_propiedad',
            field=models.CharField(choices=[('Terreno', 'Terreno'), ('Casa', 'Casa'), ('Departamento', 'Departamento')], default='CA', max_length=20),
        ),
    ]