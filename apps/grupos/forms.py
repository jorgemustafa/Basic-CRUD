from django import forms
from django.forms import ModelForm
from .models import Grupo

class GrupoForm(ModelForm):
    class Meta:
        model = Grupo
        fields = ['nome', 'cod', 'inclusao', 'user', 'ativo']
        widgets = {
            'inclusao': forms.HiddenInput,
            'ativo': forms.HiddenInput,
            # 'user': forms.HiddenInput
        }