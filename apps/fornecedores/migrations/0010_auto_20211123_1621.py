# Generated by Django 2.2 on 2021-11-23 19:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedores', '0009_auto_20211123_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedor',
            name='inclusao',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 23, 16, 21, 31, 940506), verbose_name='Inclusão'),
        ),
    ]
