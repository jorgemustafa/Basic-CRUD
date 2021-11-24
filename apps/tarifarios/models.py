from django.db import models
import datetime
from apps.clientes.models import Cliente
from apps.fornecedores.models import Fornecedor
from apps.postos.models import POS
from django.contrib.auth.models import User


class Tarifario(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Cliente')
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, verbose_name='Fornecedor')
    pos = models.ForeignKey(POS, on_delete=models.CASCADE, verbose_name='POS')
    tipoQuarto_choices = [
        ('SGL', 'Single'),
        ('DOB', 'Double'),
        ('TRP', 'Triple'),
        ('QUP', 'Quadruple'),
    ]
    tipoQuarto = models.CharField('Tipo de Apartamento', max_length=3, choices=tipoQuarto_choices)
    diaria = models.IntegerField('Valor da Diária')
    taxa = models.IntegerField('Valor das Taxas')
    tarifaQualif = models.BooleanField('Se a Tarifa é Qualificada com o Fornecedor', default=False)
    tarifaAcordo = models.BooleanField('Tarifa Acordo', default=False)
    tarifaFlut = models.BooleanField('Tarifa Flutuante', default=False)
    validade = models.DateField('Vencimento da Tarifa')
    inclusao = models.DateTimeField('Inclusão', auto_now_add=True)
    edicao = models.DateTimeField('Edição', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    ativo = models.BooleanField('Ativo', default=True)

    def __str__(self):
        return self.cliente.nome


    class Meta:
        verbose_name_plural = 'Tarifários'
        ordering = [
            'cliente'
        ]
