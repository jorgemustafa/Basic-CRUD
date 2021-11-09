from django.db import models
import datetime
from django.contrib.auth.models import User
from apps.colaboradores.models import Colaborador
from apps.grupos.models import Grupo
from apps.postos.models import POS


class Cliente(models.Model):
    nome = models.CharField('Razão Social', max_length=60)
    fantasia = models.CharField('Nome Fantasia', max_length=60)
    grupos = models.ForeignKey(Grupo, on_delete=models.CASCADE, null=True)
    executivo = models.ForeignKey(Colaborador, on_delete=models.CASCADE, null=True)
    postos = models.ForeignKey(POS, on_delete=models.CASCADE, null=True)
    vencimento = models.DateField('Data de Vencimento do Contrato')
    inclusao = models.DateTimeField('Inclusão', default=datetime.datetime.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário', null=True)
    ativo = models.BooleanField('Ativo', default=True)

    def __str__(self):
        return self.nome
