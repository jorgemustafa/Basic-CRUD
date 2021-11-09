import datetime
from django.db import models
from django.contrib.auth.models import User


class Colaborador(models.Model):
    nome = models.CharField('Nome do Colaborador', max_length=200)
    email = models.EmailField('Email do Colaborador', max_length=60)
    inclusao = models.DateTimeField('Inclusão', default=datetime.datetime.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'
        ordering = [
            'nome'
        ]

    def __str__(self):
        return self.nome
