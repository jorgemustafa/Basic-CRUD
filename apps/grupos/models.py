from django.contrib.auth.models import User
from django.db import models


class Grupo(models.Model):
    nome = models.CharField('Nome do Grupo', max_length=30,)
    cod = models.CharField('Código do Grupo', max_length=30)
    inclusao = models.DateTimeField('Inclusão', auto_now_add=True)
    edicao = models.DateTimeField('Edição', auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    ativo = models.BooleanField('Ativo', default=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Grupos'
        ordering = [
            'nome'
        ]

