from django.db import models
import datetime
from django.contrib.auth.models import User


class POS(models.Model):
    codigo = models.CharField('Codigo do Ponto de Atendimento', max_length=30)
    nome = models.CharField('Nome do Ponto de Atendimento', max_length=60)
    inclusao = models.DateTimeField('Inclusão', default=datetime.datetime.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    ativo = models.BooleanField('Ativo', default=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'POS'
        verbose_name_plural = 'POS'
        ordering = [
            'nome'
        ]

