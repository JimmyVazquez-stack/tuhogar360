# Generated by Django 4.2 on 2024-04-11 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_vendedor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tuhogar360',
            name='is_vendedorTuHogar360',
        ),
        migrations.AddField(
            model_name='vendedor',
            name='is_validado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vendedor',
            name='is_vendedorTuHogar360',
            field=models.BooleanField(default=False),
        ),
    ]
