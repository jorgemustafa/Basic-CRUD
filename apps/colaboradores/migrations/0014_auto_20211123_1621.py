# Generated by Django 2.2 on 2021-11-23 19:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colaboradores', '0013_auto_20211123_1314'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='colaborador',
            options={'ordering': ['nome'], 'verbose_name_plural': 'Colaboradores'},
        ),
        migrations.AlterField(
            model_name='colaborador',
            name='inclusao',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 23, 16, 21, 31, 936505), verbose_name='Inclusão'),
        ),
    ]