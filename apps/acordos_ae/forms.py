from django.forms import ModelForm
from .models import AcordoAereo


class AcordoForm(ModelForm):
    class Meta:
        model = AcordoAereo
        fields = ['cliente', 'grupos', 'postos', 'acordo', 'validade', 'desconto', 'destino',
                  'continente', 'inclusao', 'user', 'ativo']

class AcordoFormGol(ModelForm):
    class Meta:
        model = AcordoAereo
        fields = ['cliente', 'grupos', 'postos', 'acordo', 'validade', 'desconto', 'destino',
                  'continente', 'oac', 'inclusao', 'user', 'ativo']
