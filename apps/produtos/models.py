import datetime
from django.db import models
from django.contrib.auth.models import User


class Produto(models.Model):
    codigo = models.CharField('Codigo do Produto', max_length=2)
    nome = models.CharField('Nome do Produto', max_length=50)
    inclusao = models.DateTimeField('Inclusão', default=datetime.datetime.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    ativo = models.BooleanField('Ativo', default=True)

    def __str__(self):
        return self.nome + ' | ' + self.codigo

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = [
            'codigo'
        ]