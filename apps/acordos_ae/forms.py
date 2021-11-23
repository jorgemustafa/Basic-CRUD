from django import forms
from django.forms import ModelForm
from .models import AcordoAereo


class AcordoForm(ModelForm):
    class Meta:
        model = AcordoAereo
        fields = ['acordo', 'cliente', 'grupos', 'postos', 'validade', 'desconto', 'destino',
                  'continente', 'inclusao', 'ativo']
        widgets = {
            'validade': forms.TextInput(attrs={'type': 'date'}),
            'desconto': forms.NumberInput(attrs={'placeholder': '%'}),
            'inclusao': forms.HiddenInput,
        }


class AcordoFormGol(ModelForm):
    class Meta:
        model = AcordoAereo
        fields = ['cliente', 'grupos', 'postos', 'acordo', 'validade', 'desconto', 'destino',
                  'continente', 'inclusao', 'oac', 'ativo']
        widgets = {
            'validade': forms.DateInput(attrs={'type': 'date'}),
            'desconto': forms.NumberInput(attrs={'placeholder': '%'}),
            'inclusao': forms.HiddenInput,
        }
