# Generated by Django 2.2 on 2021-11-22 19:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fees', '0004_auto_20211122_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fee',
            name='inclusao',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 22, 16, 36, 4, 159307), verbose_name='Inclusão'),
        ),
    ]
