# Generated by Django 2.2 on 2021-11-22 18:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pos',
            name='inclusao',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 22, 15, 27, 56, 348737), verbose_name='Inclusão'),
        ),
    ]