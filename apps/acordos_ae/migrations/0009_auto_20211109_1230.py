# Generated by Django 2.2 on 2021-11-09 15:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acordos_ae', '0008_auto_20211109_1008'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='acordoaereo',
            options={'ordering': ['acordo'], 'verbose_name': 'Acordo Aéreo', 'verbose_name_plural': 'Acordos Aéreos'},
        ),
        migrations.AlterField(
            model_name='acordoaereo',
            name='inclusao',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 9, 12, 29, 45, 136372), verbose_name='Inclusão'),
        ),
    ]