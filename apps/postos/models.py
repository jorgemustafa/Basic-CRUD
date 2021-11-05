from django.db import models


class Posto(models.Model):
    codigo = models.CharField('Codigo do Ponto de Atendimento', max_length=30)
    nome = models.CharField('Nome do Ponto de Atendimento', max_length=60)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    #inclusao = models.DateTimeField(default=timezone.now)
    ativo = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

