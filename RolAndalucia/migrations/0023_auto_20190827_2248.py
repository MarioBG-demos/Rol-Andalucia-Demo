# Generated by Django 2.2.4 on 2019-08-27 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RolAndalucia', '0022_auto_20190827_2247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rule',
            old_name='parent_rule',
            new_name='parentRule',
        ),
    ]
