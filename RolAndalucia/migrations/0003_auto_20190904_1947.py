# Generated by Django 2.2.4 on 2019-09-04 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RolAndalucia', '0002_auto_20190904_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='craftable',
            name='application',
            field=models.BooleanField(default=False, verbose_name='Aplicación'),
        ),
        migrations.AddField(
            model_name='craftable',
            name='artifact',
            field=models.BooleanField(default=False, verbose_name='Artefacto'),
        ),
    ]
