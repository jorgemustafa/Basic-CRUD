from django.db import models


class Grupo(models.Model):
    nome = models.CharField('Nome do Grupo', max_length=30,)
    cod = models.CharField('Código do Grupo', max_length=30)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    #inclusao = models.DateTimeField(default=timezone.now)
    ativo = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

