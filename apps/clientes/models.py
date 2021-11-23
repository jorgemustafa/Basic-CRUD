from django.db import models
from django.contrib.auth.models import User
import datetime
from apps.colaboradores.models import Colaborador
from apps.grupos.models import Grupo
from apps.postos.models import POS


class Cliente(models.Model):
    nome = models.CharField('Razão Social', max_length=60)
    fantasia = models.CharField('Nome Fantasia', max_length=60)
    grupos = models.ForeignKey(Grupo, on_delete=models.CASCADE, verbose_name='Grupo de Clientes')
    executivo = models.ForeignKey(Colaborador, on_delete=models.CASCADE, verbose_name='Nome do Executivo')
    postos = models.ForeignKey(POS, on_delete=models.CASCADE, verbose_name='Ponto de Atendimento')
    vencimento = models.DateField('Data de Vencimento do Contrato')
    vigencia_choices = [
        ('12', '12'),
        ('24', '24'),
        ('36', '36'),
        ('48', '48'),
        ('IN', 'Indeterminado')
    ]
    vigencia = models.CharField('Período de Vigência do Contrato', choices=vigencia_choices, max_length=2, default='12')
    inclusao = models.DateTimeField('Inclusão', default=datetime.datetime.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    ativo = models.BooleanField('Ativo', default=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Clientes'
        ordering = [
            'nome'
        ]
