# Generated by Django 2.2.4 on 2019-12-09 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RolAndalucia', '0007_pertenenciaclase_nivel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pertenenciaclase',
            name='clase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RolAndalucia.CharacterClass'),
        ),
        migrations.AlterField(
            model_name='pertenenciaclase',
            name='personaje',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pertenenciasClase', to='RolAndalucia.Personaje'),
        ),
    ]
