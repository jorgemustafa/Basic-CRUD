# Generated by Django 2.2 on 2021-11-05 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60, verbose_name='Razão Social')),
                ('fantasia', models.CharField(max_length=60, verbose_name='Nome Fantasia')),
                ('vencimento', models.DateField(verbose_name='Data de Vencimento do Contrato')),
                ('ativo', models.BooleanField(default=False)),
            ],
        ),
    ]
