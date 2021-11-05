from django.contrib.auth.models import User
from django.db import models
from apps.clientes.models import Cliente
from apps.fornecedores.models import Fornecedores
from apps.grupos.models import Grupo
from apps.postos.models import Posto


class AcordoAereo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fornecedores = models.ForeignKey(Fornecedores, on_delete=models.CASCADE)
    postos = models.ForeignKey(Posto, on_delete=models.CASCADE)
    grupos = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    acordo = models.CharField('Código do Acordo do Cliente', max_length=50)
    validade = models.DateField('Validade do Acordo do Cliente')
    desconto = models.IntegerField('Percentual do Desconto')
    destino = models.CharField('Nacional ou Internacional', max_length=1)
    continente = models.CharField('Nome dos Continentes', max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #inclusao = models.DateTimeField(default=timezone.now)
    ativo = models.BooleanField(default=False)

    def __str__(self):
        return self.acordo