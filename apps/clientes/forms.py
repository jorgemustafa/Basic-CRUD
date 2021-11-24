from django import forms
from django.forms import ModelForm
from .models import Cliente


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'fantasia', 'grupos', 'executivo', 'postos', 'vencimento',
                  'vigencia', 'ativo']
        widgets = {
            'vencimento': forms.TextInput(attrs={'type': 'date'}),
        }