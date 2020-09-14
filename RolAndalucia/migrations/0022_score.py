# Generated by Django 3.1 on 2020-08-13 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RolAndalucia', '0021_auto_20191223_2008'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=64)),
                ('enabled', models.BooleanField(default=False)),
                ('statBlock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores', to='RolAndalucia.statblock')),
            ],
        ),
    ]