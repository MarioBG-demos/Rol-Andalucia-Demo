# Generated by Django 2.2.4 on 2019-12-15 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RolAndalucia', '0012_personaje_descripcion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='spell',
            options={'ordering': ['level', 'school', 'name']},
        ),
        migrations.AddField(
            model_name='trabajo',
            name='visible',
            field=models.BooleanField(default=False),
        ),
    ]
