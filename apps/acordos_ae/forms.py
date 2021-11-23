from django import forms
from django.forms import ModelForm
from .models import AcordoAereo


class AcordoForm(ModelForm):
    class Meta:
        model = AcordoAereo
        fields = ['cliente', 'grupos', 'postos', 'acordo', 'validade', 'desconto', 'destino',
                  'continente', 'inclusao', 'user', 'ativo']
        widgets = {
            'validade': forms.TextInput(attrs={'type': 'date'}),
            'desconto': forms.NumberInput(attrs={'placeholder': '%'}),
            'inclusao': forms.HiddenInput,
            'ativo': forms.HiddenInput,
            # 'user': forms.HiddenInput,
        }


class AcordoFormGol(ModelForm):
    class Meta:
        model = AcordoAereo
        fields = ['cliente', 'grupos', 'postos', 'acordo', 'validade', 'desconto', 'destino',
                  'continente', 'oac', 'inclusao', 'user', 'ativo']
        widgets = {
            'validade': forms.DateInput(attrs={'type': 'date'}),
            'desconto': forms.NumberInput(attrs={'placeholder': '%'}),
            'inclusao': forms.HiddenInput,
            'ativo': forms.HiddenInput,
            # 'user': forms.HiddenInput,
        }
