# Generated by Django 2.2 on 2021-11-22 19:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedores', '0006_auto_20211122_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedor',
            name='inclusao',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 22, 16, 56, 28, 533456), verbose_name='Inclusão'),
        ),
    ]
