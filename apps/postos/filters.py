import django_filters
from django_filters import CharFilter
from .models import POS


class POSFilter(django_filters.FilterSet):
    cod = CharFilter(field_name='codigo', lookup_expr='icontains')
    nome = CharFilter(field_name='nome', lookup_expr='icontains')