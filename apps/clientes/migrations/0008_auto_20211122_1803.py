# Generated by Django 2.2 on 2021-11-22 21:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0007_auto_20211122_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='inclusao',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 22, 18, 3, 25, 487924), verbose_name='Inclusão'),
        ),
    ]
