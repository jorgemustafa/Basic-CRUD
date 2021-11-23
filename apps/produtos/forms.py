from django import forms
from django.forms import ModelForm
from .models import Produto

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'codigo', 'inclusao', 'ativo']
        widgets = {
            'inclusao': forms.HiddenInput,
        }