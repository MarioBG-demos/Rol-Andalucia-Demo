# Generated by Django 2.2 on 2021-08-10 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RolAndalucia', '0028_auto_20210810_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='hiRes',
            field=models.CharField(max_length=240, verbose_name='Alta resolución'),
        ),
        migrations.AlterField(
            model_name='foto',
            name='lowRes',
            field=models.CharField(max_length=240, verbose_name='Baja resolución'),
        ),
    ]
