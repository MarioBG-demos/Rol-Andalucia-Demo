# Generated by Django 2.2.4 on 2019-08-28 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RolAndalucia', '0029_auto_20190828_1218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rule',
            name='parentId',
        ),
    ]
