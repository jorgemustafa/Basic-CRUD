# Generated by Django 2.2 on 2021-11-23 14:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0010_auto_20211123_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='inclusao',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 23, 11, 0, 43, 996756), verbose_name='Inclusão'),
        ),
    ]
