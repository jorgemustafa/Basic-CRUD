# Generated by Django 2.2 on 2021-11-05 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colaboradores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome do Colaborador')),
                ('email', models.CharField(max_length=60, verbose_name='Email do Colaborador')),
                ('ativo', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Colaboradores',
                'verbose_name': 'Colaborador',
                'ordering': ['nome'],
            },
        ),
    ]
