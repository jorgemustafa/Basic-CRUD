import django_filters
from django_filters import CharFilter


class ProdutoFilter(django_filters.FilterSet):
    nome = CharFilter(field_name='nome', lookup_expr='icontains')
    cod = CharFilter(field_name='codigo', lookup_expr='icontains')
