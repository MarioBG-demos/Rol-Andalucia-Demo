# Generated by Django 3.1 on 2020-08-13 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RolAndalucia', '0023_ability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ability',
            name='habilidadPadre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='RolAndalucia.ability'),
        ),
    ]
