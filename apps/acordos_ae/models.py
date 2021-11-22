import datetime
from django.contrib.auth.models import User
from django.db import models
from apps.clientes.models import Cliente
from apps.fornecedores.models import Fornecedor
from apps.grupos.models import Grupo
from apps.postos.models import POS


class AcordoAereo(models.Model):

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Nome do Cliente')
    grupos = models.ForeignKey(Grupo, on_delete=models.CASCADE, verbose_name='Grupo do Cliente')
    fornecedores = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, verbose_name='Fornecedor')
    oac = models.CharField('OAC', max_length=10, null=True)
    postos = models.ForeignKey(POS, on_delete=models.CASCADE, verbose_name='POS')
    acordo = models.CharField('Código do Acordo do Cliente', max_length=50)
    validade = models.DateField('Validade do Acordo do Cliente')
    desconto = models.IntegerField('Percentual do Desconto')
    destino_choices = [
        ('N','Nacional'),
        ('I','Internacional'),
    ]
    destino = models.CharField('Nacional ou Internacional', max_length=1, choices=destino_choices)
    continente_choices = [
        ('AM', 'América'),
        ('AF', 'África'),
        ('EU', 'Europa'),
        ('OC', 'Oceania'),
        ('AS', 'Ásia'),
    ]
    continente = models.CharField('Nome dos Continentes', max_length=2, choices=continente_choices)
    inclusao = models.DateTimeField('Inclusão', default=datetime.datetime.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    ativo = models.BooleanField('Ativo', default=True)

    def __str__(self):
        return self.acordo


    class Meta:
        verbose_name = 'Acordo Aéreo'
        verbose_name_plural = 'Acordos Aéreos'
        ordering = [
            'acordo'
        ]
