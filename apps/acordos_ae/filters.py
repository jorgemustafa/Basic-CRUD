import django_filters
from django_filters import CharFilter
from .models import AcordoAereo


class AcordoFilter(django_filters.FilterSet):
    acordo = CharFilter(field_name='acordo', lookup_expr='icontains')
    cliente = CharFilter(field_name='cliente__nome', lookup_expr='icontains')

    class Meta:
        model = AcordoAereo
        fields = ['fornecedores']
