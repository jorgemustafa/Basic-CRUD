# Generated by Django 2.2 on 2021-11-23 20:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarifarios', '0014_auto_20211123_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarifario',
            name='inclusao',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 23, 17, 7, 33, 780514), verbose_name='Inclusão'),
        ),
    ]