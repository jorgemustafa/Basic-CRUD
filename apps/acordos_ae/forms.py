from django.forms import ModelForm
from .models import AcordoAereo

class AcordoForm(ModelForm):
    class Meta:
        model = AcordoAereo
        fields = ['cliente', 'grupos', 'fornecedores', 'postos', 'acordo', 'validade', 'desconto', 'destino', 'continente', 'inclusao', 'user', 'ativo']
