# Generated by Django 2.2 on 2021-11-23 14:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colaboradores', '0011_auto_20211123_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='inclusao',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 23, 11, 4, 19, 909477), verbose_name='Inclusão'),
        ),
    ]
