# Generated by Django 2.2 on 2021-11-24 14:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fees', '0016_auto_20211124_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fee',
            name='inclusao',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 24, 11, 35, 48, 39615), verbose_name='Inclusão'),
        ),
    ]
