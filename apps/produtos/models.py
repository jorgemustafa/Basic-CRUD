from django.db import models

class Produto(models.Model):
    codigo = models.CharField('Codigo do Produto', max_length=2)
    nome = models.CharField('Nome do Produto', max_length=50)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    #inclusao = models.DateTimeField(default=timezone.now)
    ativo = models.BooleanField(default=False)
