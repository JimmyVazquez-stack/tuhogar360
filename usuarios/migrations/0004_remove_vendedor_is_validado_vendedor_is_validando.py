# Generated by Django 4.2 on 2024-04-16 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_remove_tuhogar360_is_vendedortuhogar360_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendedor',
            name='is_validado',
        ),
        migrations.AddField(
            model_name='vendedor',
            name='is_validando',
            field=models.BooleanField(default=True),
        ),
    ]