# Generated by Django 2.2 on 2021-11-24 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fees', '0017_auto_20211124_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fee',
            name='inclusao',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Inclusão'),
        ),
    ]