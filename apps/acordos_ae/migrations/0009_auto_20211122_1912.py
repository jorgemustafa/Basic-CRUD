# Generated by Django 2.2 on 2021-11-22 22:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acordos_ae', '0008_auto_20211122_1803'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='acordoaereo',
            options={'ordering': ['acordo'], 'verbose_name_plural': 'Acordos Aéreos'},
        ),
        migrations.AlterField(
            model_name='acordoaereo',
            name='inclusao',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 22, 19, 12, 26, 432407), verbose_name='Inclusão'),
        ),
    ]
