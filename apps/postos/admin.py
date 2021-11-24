from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import POS

@admin.register(POS)
class POSAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'user', 'ativo',)

    list_filter = ('codigo', 'nome', 'inclusao', 'user', 'ativo',)

    search_fields = ('codigo', 'nome',)

    readonly_fields = ('inclusao', 'edicao',)
