from django import forms
from django.forms import ModelForm
from .models import Fee


class FeeForm(ModelForm):
    class Meta:
        model = Fee
        fields = ['cliente', 'aenacon', 'aeinton', 'honacon', 'hointon', 'canacon', 'cainton',
                  'aenacoff', 'aeintoff', 'honacoff', 'hointoff', 'canacoff', 'caintoff', 'vip',
                  'doc', 'fer', 'emergencial', 'ateae', 'segViagem', 'passRod', 'reembolso',
                  'cancelamento', 'assentoConf', 'implantacao', 'treinamento', 'consultoria',
                  'expense', 'eventos', 'demais', 'renovacao', 'ativo']
        widgets = {
            'aenacon': forms.NumberInput(attrs={'placeholder': 'R$'}),
            'aeinton': forms.NumberInput(attrs={'placeholder': 'R$'}),
            'honacon': forms.NumberInput(attrs={'placeholder': 'R$'}),
            'hointon': forms.NumberInput(attrs={'placeholder': 'R$'}),
            'canacon': forms.NumberInput(attrs={'placeholder': 'R$'}),
            'cainton': forms.NumberInput(attrs={'placeholder': 'R$'}),
            'aenacoff': forms.NumberInput(attrs={'placeholder': 'R$'}),
            'aeintoff': forms.NumberInput(attrs={'placeholder': 'R$'}),
            'honacoff': forms.NumberInput(attrs={'placeholder': 'R$'}),
            'hointoff': forms.NumberInput(attrs={'placeholder': 'R$'}),
            'canacoff': forms.NumberInput(attrs={'placeholder': 'R$'}),
            'caintoff': forms.NumberInput(attrs={'placeholder': 'R$'}),
            'vip': forms.NumberInput(attrs={'placeholder': 'R$'}),
            'doc': forms.NumberInput(attrs={'placeholder': 'R$'}),
            'fer': forms.NumberInput(attrs={'placeholder': 'R$'}),
            'emergencial': forms.NumberInput(attrs={'placeholder': 'R$'}),
            'ateae': forms.NumberInput(attrs={'placeholder': 'R$'}),
            'segViagem': forms.NumberInput(attrs={'placeholder': 'R$'}),
            'passRod': forms.NumberInput(attrs={'placeholder': 'R$'}),
            'reembolso': forms.NumberInput(attrs={'placeholder': 'R$'}),
            'cancelamento': forms.NumberInput(attrs={'placeholder': 'R$'}),
            'assentoConf': forms.NumberInput(attrs={'placeholder': 'R$'}),
            'implantacao': forms.NumberInput(attrs={'placeholder': 'R$'}),
            'treinamento': forms.NumberInput(attrs={'placeholder': 'R$'}),
            'consultoria': forms.NumberInput(attrs={'placeholder': 'R$'}),
            'expense': forms.NumberInput(attrs={'placeholder': 'R$'}),
            'eventos': forms.NumberInput(attrs={'placeholder': 'R$'}),
            'demais': forms.NumberInput(attrs={'placeholder': 'R$'}),
            'renovacao': forms.TextInput(attrs={'type': 'date'}),
        }