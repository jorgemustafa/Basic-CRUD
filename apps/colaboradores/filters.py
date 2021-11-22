import django_filters
from django_filters import CharFilter
from .models import Colaborador


class ColaboradorFilter(django_filters.FilterSet):
    nome = CharFilter(field_name='nome', lookup_expr='icontains')

    class Meta:
        model = Colaborador
        fields = ['email']
