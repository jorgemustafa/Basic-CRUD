from django.db import models
from apps.clientes.models import Cliente


class Fee(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Nome do Cliente', null=True)
    aenacon = models.IntegerField('Valor do Fee - Aéreo Nacional Online')
    aeinton = models.IntegerField('Valor do Fee - Aéreo Internacional Online')
    honacon = models.IntegerField('Valor do Fee - Hotel Nacional Online')
    hointon = models.IntegerField('Hotel Internacional Online')
    canacon = models.IntegerField('Carro Nacional Online')
    cainton = models.IntegerField('Carro Internacional Online')
    aenacoff = models.IntegerField('Aéreo Nacional OffLine')
    aeintoff = models.IntegerField('Aéreo Internacional OffLine')
    honacoff = models.IntegerField('Hotel Nacional OffLine')
    hointoff = models.IntegerField('Hotel Internacional OffLine')
    canacoff = models.IntegerField('Carro Nacional OffLine')
    caintoff = models.IntegerField('Carro Internacional OffLine')
    vip = models.IntegerField('Vip House')
    doc = models.IntegerField('Documentação')
    fer = models.IntegerField('Passagem Ferroviária')
    emergencial = models.IntegerField('Atendimento Emergencial')
    ateae = models.IntegerField('Atendimento Aeroporto')
    segViagem = models.IntegerField('Seguro Viagem')
    passRod = models.IntegerField('Passagem Rodoviária')
    reembolso = models.IntegerField('Reembolso')
    cancelamento = models.IntegerField('Cancelamento')
    assentoConf = models.IntegerField('Assento Conforto')
    implantacao = models.IntegerField('Implantação')
    treinamento = models.IntegerField('Treinamento')
    consultoria = models.IntegerField('Gestão de Consultoria')
    expense = models.IntegerField('Expense')
    eventos = models.IntegerField('Eventos')
    demais = models.IntegerField('Demais Serviços')
    renovacao = models.DateTimeField('Data para a Renovação do valor Fee')
    #user = models.ForeignKey(User, on_delete=models.CASCADE,help_text='Usuário da Inclusão')
    #inclusao = models.DateTimeField(default=timezone.now)
    ativo = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Fee'
        verbose_name_plural = 'Fees'
        ordering = [
            'cliente'
        ]

    def __str__(self):
         return self.cliente