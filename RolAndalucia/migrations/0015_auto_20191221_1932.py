# Generated by Django 2.2.4 on 2019-12-21 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RolAndalucia', '0014_auto_20191220_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryentry',
            name='personaje',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventoryEntries', to='RolAndalucia.Personaje'),
        ),
    ]
