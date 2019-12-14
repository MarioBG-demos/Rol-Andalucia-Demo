# Generated by Django 2.2.4 on 2019-12-06 23:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RolAndalucia', '0006_auto_20191206_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='pertenenciaclase',
            name='nivel',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
    ]