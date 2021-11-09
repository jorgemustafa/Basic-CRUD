from django.db import models

class Tarifario(models.Model):
    #cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    #fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    #grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    #pos = models.ForeignKey(POS, on_delete=models.CASCADE)
    tipoQuarto = models.CharField('Tipo de Apartamento', max_length=3)
    tarifaQualif = models.BooleanField('Se a Tarifa é Qualificada com o Fornecedor', default=False)
    diaria = models.IntegerField('Valor da Diária')
    taxa = models.IntegerField('Valor das Taxas')
    tarifaAcordo = models.BooleanField('Tarifa Acordo', default=False)
    tarifaFlut = models.BooleanField('Tarifa Flutuante', default=False)
    #validade = models.DateTimeField('Vencimento da Tarifa')
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    #inclusao = models.DateTimeField(default=timezone.now)
    ativo = models.BooleanField(default=False)


