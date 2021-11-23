from django.contrib import admin
from .models import Fornecedor

@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'fantasia', 'rede', 'produtos', 'user', 'ativo',)

    list_filter = ('nome', 'fantasia', 'rede', 'produtos', 'user', 'ativo',)

    search_fields = ('nome', 'fantasia', 'rede', 'produtos__nome')
