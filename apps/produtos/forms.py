from django import forms
from django.forms import ModelForm
from .models import Produto

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = [ 'nome', 'codigo', 'inclusao', 'user', 'ativo']
        widgets = {
            'inclusao': forms.HiddenInput,
            'ativo': forms.HiddenInput,
            # 'user': forms.HiddenInput
        }