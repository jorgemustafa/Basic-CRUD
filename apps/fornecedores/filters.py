import django_filters
from django_filters import CharFilter
from .models import Fornecedor


class FornecedorFilter(django_filters.FilterSet):
    nome = CharFilter(field_name='nome', lookup_expr='icontains')

    class Meta:
        model = Fornecedor
        fields = ['produtos']