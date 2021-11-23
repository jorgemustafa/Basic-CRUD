from django import forms
from django.forms import ModelForm
from .models import Tarifario


class TarifarioForm(ModelForm):
    class Meta:
        model = Tarifario
        fields = ['cliente', 'fornecedor', 'pos', 'tipoQuarto', 'diaria', 'validade',
                  'taxa', 'tarifaQualif', 'tarifaAcordo', 'tarifaFlut', 'inclusao', 'user', 'ativo']
        widgets = {
            'validade': forms.TextInput(attrs={'type': 'date'}),
            'diaria': forms.NumberInput(attrs={'placeholder': 'R$'}),
            'taxa': forms.NumberInput(attrs={'placeholder': 'R$'}),
            'inclusao': forms.HiddenInput,
            'ativo': forms.HiddenInput,
            # 'user': forms.HiddenInput,
        }
