# Generated by Django 2.2.4 on 2019-11-29 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RolAndalucia', '0004_personaje_trabajo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaje',
            name='clase',
            field=models.ManyToManyField(to='RolAndalucia.CharacterClass', verbose_name='Clase principal'),
        ),
    ]
