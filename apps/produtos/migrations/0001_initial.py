# Generated by Django 2.2 on 2021-11-22 18:27

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=2, verbose_name='Codigo do Produto')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome do Produto')),
                ('inclusao', models.DateTimeField(default=datetime.datetime(2021, 11, 22, 15, 27, 27, 570194), verbose_name='Inclusão')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'ordering': ['codigo'],
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
    ]
