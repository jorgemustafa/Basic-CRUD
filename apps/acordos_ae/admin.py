from django.contrib import admin
from .models import AcordoAereo


@admin.register(AcordoAereo)
class AcordoAereoAdmin(admin.ModelAdmin):
    list_display = ('acordo', 'cliente', 'grupos', 'fornecedores', 'postos',
                    'validade', 'desconto', 'destino', 'continente', 'user', 'ativo',)

    list_filter = ('cliente', 'grupos', 'fornecedores', 'postos', 'destino', 'continente', 'inclusao', 'user', 'ativo',)

    search_fields = ('cliente__nome', 'grupos__nome', 'fornecedores__nome', 'oac', 'postos__nome', 'acordo',
                     'validade', 'desconto', 'destino', 'continente',)
