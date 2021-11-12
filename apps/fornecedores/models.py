import datetime
from django.contrib.auth.models import User
from django.db import models
from apps.produtos.models import Produto


class Fornecedor(models.Model):
    nome = models.CharField('Razão Social', max_length=60)
    fantasia = models.CharField('Nome Fantasia', max_length=60)
    rede = models.CharField('Grupo do Fornecedor', max_length=60)
    produtos = models.ForeignKey(Produto, on_delete=models.CASCADE, verbose_name='Produtos')
    inclusao = models.DateTimeField('Inclusão', default=datetime.datetime.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        ordering = [
            'nome'
        ]

    def __str__(self):
        return self.nome
