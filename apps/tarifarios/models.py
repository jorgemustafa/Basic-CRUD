from django.db import models
import datetime
from apps.clientes.models import Cliente
from apps.fornecedores.models import Fornecedor
from apps.grupos.models import Grupo
from apps.postos.models import POS
from django.contrib.auth.models import User


class Tarifario(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    pos = models.ForeignKey(POS, on_delete=models.CASCADE)
    tipoQuarto = models.CharField('Tipo de Apartamento', max_length=3)
    tarifaQualif = models.BooleanField('Se a Tarifa é Qualificada com o Fornecedor', default=False)
    diaria = models.IntegerField('Valor da Diária')
    taxa = models.IntegerField('Valor das Taxas')
    tarifaAcordo = models.BooleanField('Tarifa Acordo', default=False)
    tarifaFlut = models.BooleanField('Tarifa Flutuante', default=False)
    validade = models.DateTimeField('Vencimento da Tarifa')
    inclusao = models.DateTimeField('Inclusão', default=datetime.datetime.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    ativo = models.BooleanField('Ativo', default=True)

    def __str__(self):
        return self.cliente

    class Meta:
        verbose_name = 'Tarifário'
        verbose_name_plural = 'Tarifários'
        ordering = [
            'cliente'
        ]
