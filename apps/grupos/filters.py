import django_filters
from django_filters import CharFilter
from .models import Grupo


class GrupoFilter(django_filters.FilterSet):
    nome = CharFilter(field_name='nome', lookup_expr='icontains')
    cod = CharFilter(field_name='cod', lookup_expr='icontains')
