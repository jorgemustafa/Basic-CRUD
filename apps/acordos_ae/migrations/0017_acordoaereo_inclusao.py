# Generated by Django 2.2 on 2021-11-24 14:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('acordos_ae', '0016_remove_acordoaereo_inclusao'),
    ]

    operations = [
        migrations.AddField(
            model_name='acordoaereo',
            name='inclusao',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 11, 24, 14, 36, 2, 579619, tzinfo=utc), verbose_name='Inclusão'),
            preserve_default=False,
        ),
    ]
