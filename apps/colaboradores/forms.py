from django import forms
from django.forms import ModelForm
from .models import Colaborador


class ColaboradorForm(ModelForm):
    class Meta:
        model = Colaborador
        fields = ['nome', 'email', 'ativo']
        widgets = {
            'email': forms.EmailInput(attrs={'type':'email', 'placeholder':'nome@tourhouse.com.br'}),
        }