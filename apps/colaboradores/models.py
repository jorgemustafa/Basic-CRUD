from django.db import models


class Colaborador(models.Model):
    nome = models.CharField('Nome do Colaborador', max_length=200)
    email = models.CharField('Email do Colaborador', max_length=60)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    #inclusao = models.DateTimeField(default=timezone.now)
    ativo = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'
        ordering = [
            'nome'
        ]

    def __str__(self):
        return self.nome
