import django_filters
from django_filters import CharFilter
from .models import Tarifario


class TarifarioFilter(django_filters.FilterSet):
    cliente = CharFilter(field_name='cliente__nome', lookup_expr='icontains')
    fornecedor = CharFilter(field_name='fornecedor__nome', lookup_expr='icontains')

    class Meta:
        model = Tarifario
        fields = ['pos', 'tipoQuarto']