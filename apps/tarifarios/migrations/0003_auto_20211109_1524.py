# Generated by Django 2.2 on 2021-11-09 18:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarifarios', '0002_auto_20211109_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarifario',
            name='inclusao',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 9, 15, 24, 26, 323541), verbose_name='Inclusão'),
        ),
    ]
