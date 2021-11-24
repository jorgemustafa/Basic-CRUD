from django.contrib import admin
from apps.clientes.models import Cliente
from import_export.admin import ImportExportModelAdmin

@admin.register(Cliente)
class ClienteAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = ('nome', 'fantasia', 'executivo', 'postos',
                    'vencimento', 'vigencia', 'user', 'ativo',)


    list_filter = ('nome', 'executivo', 'postos', 'vigencia', 'user', 'ativo',)

    search_fields = ('nome', 'fantasia', 'grupos__nome', 'executivo__nome', 'postos__nome')

    readonly_fields = ('inclusao', 'edicao',)