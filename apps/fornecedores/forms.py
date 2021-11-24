from django import forms
from django.forms import ModelForm
from .models import Fornecedor


class FornecedorForm(ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome', 'fantasia', 'rede', 'produtos', 'ativo']
