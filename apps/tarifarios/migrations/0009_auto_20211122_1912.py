# Generated by Django 2.2 on 2021-11-22 22:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarifarios', '0008_auto_20211122_1803'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tarifario',
            options={'ordering': ['cliente'], 'verbose_name_plural': 'Tarifários'},
        ),
        migrations.AlterField(
            model_name='tarifario',
            name='inclusao',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 22, 19, 12, 26, 435407), verbose_name='Inclusão'),
        ),
    ]