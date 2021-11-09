# from datetime import timezone
from django.db import models


class Fornecedor(models.Model):
    nome = models.CharField('Razão Social', max_length=60)
    fantasia = models.CharField('Nome Fantasia', max_length=60)
    rede = models.CharField('Grupo do Fornecedor', max_length=60)
    # produtos = models.ForeignKey(on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # inclusao = models.DateTimeField(default=timezone.now)
    ativo = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        ordering = [
            'nome'
        ]
