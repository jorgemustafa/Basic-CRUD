# Generated by Django 2.2 on 2021-11-23 16:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedores', '0008_auto_20211122_1803'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fornecedor',
            options={'ordering': ['nome'], 'verbose_name_plural': 'Fornecedores'},
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='inclusao',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 23, 13, 14, 56, 368213), verbose_name='Inclusão'),
        ),
    ]
