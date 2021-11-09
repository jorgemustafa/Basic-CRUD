# Generated by Django 2.2 on 2021-11-09 15:33

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedores', '0004_auto_20211109_1233'),
        ('grupos', '0003_auto_20211109_1233'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clientes', '0011_auto_20211109_1233'),
        ('postos', '0002_auto_20211109_1233'),
        ('tarifarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tarifario',
            options={'ordering': ['cliente'], 'verbose_name': 'Tarifário', 'verbose_name_plural': 'Tarifários'},
        ),
        migrations.AddField(
            model_name='tarifario',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='clientes.Cliente'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tarifario',
            name='fornecedor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='fornecedores.Fornecedor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tarifario',
            name='grupo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='grupos.Grupo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tarifario',
            name='inclusao',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 9, 12, 33, 34, 23649), verbose_name='Inclusão'),
        ),
        migrations.AddField(
            model_name='tarifario',
            name='pos',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='postos.POS'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tarifario',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tarifario',
            name='validade',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 9, 12, 33, 34, 23649), verbose_name='Vencimento da Tarifa'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tarifario',
            name='ativo',
            field=models.BooleanField(default=True, verbose_name='Ativo'),
        ),
    ]
