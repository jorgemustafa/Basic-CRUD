#from datetime import timezone
from django.db import models

class Fornecedores(models.Model):
    nome = models.CharField(max_length=60, help_text='Razão Social')
    fantasia = models.CharField(max_length=60, help_text='Nome Fantasia')
    rede = models.CharField(max_length=60, help_text='Grupo do Fornecedor')
    #produtos = models.ForeignKey(on_delete=models.CASCADE)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    #inclusao = models.DateTimeField(default=timezone.now)
    ativo = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        ordering = [
            'nome'
        ]
