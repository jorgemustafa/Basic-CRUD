# Generated by Django 2.2 on 2021-11-09 12:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acordos_ae', '0004_auto_20211109_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acordoaereo',
            name='destino',
            field=models.CharField(choices=[('N', 'Nacional'), ('I', 'Internacional')], max_length=1, verbose_name='Nacional ou Internacional'),
        ),
        migrations.AlterField(
            model_name='acordoaereo',
            name='inclusao',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 9, 9, 59, 23, 595696), verbose_name='Inclusão'),
        ),
    ]