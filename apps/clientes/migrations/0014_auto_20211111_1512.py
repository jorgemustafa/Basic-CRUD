# Generated by Django 2.2 on 2021-11-11 18:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0013_auto_20211111_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='inclusao',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 11, 15, 12, 25, 131609), verbose_name='Inclusão'),
        ),
    ]
