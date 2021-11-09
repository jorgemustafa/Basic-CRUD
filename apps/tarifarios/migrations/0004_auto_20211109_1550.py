# Generated by Django 2.2 on 2021-11-09 18:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarifarios', '0003_auto_20211109_1524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarifario',
            name='grupo',
        ),
        migrations.AlterField(
            model_name='tarifario',
            name='inclusao',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 9, 15, 50, 25, 796645), verbose_name='Inclusão'),
        ),
        migrations.AlterField(
            model_name='tarifario',
            name='validade',
            field=models.DateField(verbose_name='Vencimento da Tarifa'),
        ),
    ]
