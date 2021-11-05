# Generated by Django 2.2 on 2021-11-05 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarifario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoQuarto', models.CharField(max_length=3, verbose_name='Tipo de Apartamento')),
                ('tarifaQualif', models.BooleanField(default=False, verbose_name='Se a Tarifa é Qualificada com o Fornecedor')),
                ('diaria', models.IntegerField(verbose_name='Valor da Diária')),
                ('taxa', models.IntegerField(verbose_name='Valor das Taxas')),
                ('tarifaAcordo', models.BooleanField(default=False, verbose_name='Tarifa Acordo')),
                ('tarifaFlut', models.BooleanField(default=False, verbose_name='Tarifa Flutuante')),
                ('ativo', models.BooleanField(default=False)),
            ],
        ),
    ]
