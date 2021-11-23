from django import forms
from django.forms import ModelForm
from .models import POS

class PostoForm(ModelForm):
    class Meta:
        model = POS
        fields = ['codigo', 'nome', 'inclusao', 'ativo']
        widgets = {
            'inclusao': forms.HiddenInput,
        }
