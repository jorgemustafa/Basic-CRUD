# Generated by Django 2.2 on 2021-11-23 16:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fees', '0012_auto_20211123_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fee',
            name='inclusao',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 23, 13, 14, 56, 370213), verbose_name='Inclusão'),
        ),
    ]
