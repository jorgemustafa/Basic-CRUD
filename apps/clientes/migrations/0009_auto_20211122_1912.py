# Generated by Django 2.2 on 2021-11-22 22:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0008_auto_20211122_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='inclusao',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 22, 19, 12, 26, 430406), verbose_name='Inclusão'),
        ),
    ]
