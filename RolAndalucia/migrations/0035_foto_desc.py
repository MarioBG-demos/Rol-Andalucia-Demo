# Generated by Django 2.2 on 2021-08-11 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RolAndalucia', '0034_auto_20210811_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='foto',
            name='desc',
            field=models.CharField(blank=True, max_length=32, verbose_name='Asunto'),
        ),
    ]
