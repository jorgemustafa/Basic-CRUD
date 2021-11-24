from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Fornecedor

@admin.register(Fornecedor)
class FornecedorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nome', 'fantasia', 'rede', 'produtos', 'user', 'ativo',)

    list_filter = ('nome', 'fantasia', 'rede', 'produtos', 'user', 'ativo',)

    search_fields = ('nome', 'fantasia', 'rede', 'produtos__nome')

    readonly_fields = ('inclusao', 'edicao',)

