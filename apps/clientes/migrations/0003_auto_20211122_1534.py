# Generated by Django 2.2 on 2021-11-22 18:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20211122_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='inclusao',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 22, 15, 34, 44, 813511), verbose_name='Inclusão'),
        ),
    ]
