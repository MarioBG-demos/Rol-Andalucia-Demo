# Generated by Django 2.2.4 on 2019-12-06 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RolAndalucia', '0005_auto_20191129_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personaje',
            name='clase',
        ),
        migrations.CreateModel(
            name='PertenenciaClase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clase', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='RolAndalucia.CharacterClass')),
                ('personaje', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pertenenciasClase', to='RolAndalucia.Personaje')),
            ],
        ),
    ]