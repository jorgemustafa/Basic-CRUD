# Generated by Django 2.2 on 2021-11-11 14:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grupos', '0004_auto_20211109_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo',
            name='inclusao',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 11, 11, 16, 56, 775028), verbose_name='Inclusão'),
        ),
    ]
