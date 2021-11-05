from django.db import models

class Cliente(models.Model):
    nome = models.CharField('Razão Social', max_length=60)
    fantasia = models.CharField('Nome Fantasia',max_length=60)
    #grupos = models.ForeignKey(Grupo, on_delete=models.CASCADE, null=True)
    #executivo = models.ForeignKey(Colaboradores, on_delete=models.CASCADE, null=True)
    #postos = models.ForeignKey(Pos, on_delete=models.CASCADE)
    vencimento = models.DateField('Data de Vencimento do Contrato')
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    #inclusao = models.DateTimeField(default=timezone.now)
    ativo = models.BooleanField(default=False)

    def __str__(self):
        return self.nome