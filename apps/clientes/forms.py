from django.forms import ModelForm
from .models import Cliente


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'fantasia', 'grupos', 'executivo', 'postos', 'vencimento', 'vigencia', 'inclusao', 'user', 'ativo']