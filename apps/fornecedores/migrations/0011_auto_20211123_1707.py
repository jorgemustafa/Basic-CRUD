# Generated by Django 2.2 on 2021-11-23 20:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedores', '0010_auto_20211123_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedor',
            name='inclusao',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 23, 17, 7, 33, 777513), verbose_name='Inclusão'),
        ),
    ]
