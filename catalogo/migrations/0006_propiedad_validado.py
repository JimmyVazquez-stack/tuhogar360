# Generated by Django 5.0.6 on 2024-05-30 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0005_alter_propiedad_fecha_publicacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='propiedad',
            name='validado',
            field=models.BooleanField(default=False),
        ),
    ]
