# Generated by Django 2.2 on 2021-11-24 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedores', '0014_auto_20211124_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='fornecedor',
            name='edicao',
            field=models.DateTimeField(auto_now=True, verbose_name='Edição'),
        ),
    ]
