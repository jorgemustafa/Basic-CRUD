from django.forms import ModelForm
from .models import Tarifario

class TarifarioForm(ModelForm):
    class Meta:
        model = Tarifario
        fields = ['cliente', 'fornecedor', 'pos', 'tipoQuarto', 'tarifaQualif', 'diaria', 'taxa', 'tarifaAcordo', 'tarifaFlut', 'validade', 'inclusao','user', 'ativo']
