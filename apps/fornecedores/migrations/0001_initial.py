# Generated by Django 2.2 on 2021-11-22 18:27

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60, verbose_name='Razão Social')),
                ('fantasia', models.CharField(max_length=60, verbose_name='Nome Fantasia')),
                ('rede', models.CharField(max_length=60, verbose_name='Grupo do Fornecedor')),
                ('inclusao', models.DateTimeField(default=datetime.datetime(2021, 11, 22, 15, 27, 27, 571194), verbose_name='Inclusão')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('produtos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.Produto', verbose_name='Produtos')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'ordering': ['nome'],
                'verbose_name': 'Fornecedor',
                'verbose_name_plural': 'Fornecedores',
            },
        ),
    ]
