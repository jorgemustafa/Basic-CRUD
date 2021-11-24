from django import forms
from django.forms import ModelForm
from .models import Grupo

class GrupoForm(ModelForm):
    class Meta:
        model = Grupo
        fields = ['nome', 'cod', 'ativo']
