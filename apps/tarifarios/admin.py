from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Tarifario

@admin.register(Tarifario)
class AcordoAereoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('cliente', 'fornecedor', 'pos', 'tipoQuarto', 'diaria', 'taxa', 'tarifaQualif',
                    'tarifaFlut', 'validade', 'user', 'ativo',)

    list_filter = ('cliente', 'fornecedor', 'pos', 'tipoQuarto', 'inclusao', 'user', 'ativo',)

    search_fields = ('cliente__nome', 'fornecedor__nome', 'pos__nome', 'tipoQuarto', 'diaria', 'taxa', 'tarifaQualif',
                    'tarifaFlut', 'validade')

    readonly_fields = ('inclusao', 'edicao',)

