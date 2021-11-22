import django_filters
from .models import Fee


class FeeFilter(django_filters.FilterSet):

    class Meta:
        model = Fee
        fields = ['cliente']
