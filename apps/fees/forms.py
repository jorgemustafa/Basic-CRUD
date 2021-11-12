from django.forms import ModelForm
from .models import Fee


class FeeForm(ModelForm):
    class Meta:
        model = Fee
        fields = ['cliente', 'aenacon', 'aeinton', 'honacon', 'hointon', 'canacon', 'cainton', 'aenacoff',
                  'aeintoff', 'honacoff', 'hointoff','canacoff', 'caintoff', 'vip', 'doc', 'fer', 'emergencial',
                  'ateae', 'segViagem', 'passRod', 'reembolso', 'cancelamento', 'assentoConf', 'implantacao',
                  'treinamento', 'consultoria', 'expense', 'eventos', 'demais', 'renovacao', 'inclusao', 'user', 'ativo']