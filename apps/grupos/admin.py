from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Grupo

@admin.register(Grupo)
class GrupoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nome', 'cod', 'user', 'ativo',)

    list_filter = ('nome', 'cod', 'inclusao', 'user', 'ativo',)

    search_fields = ('nome', 'cod')

    readonly_fields = ('inclusao', 'edicao',)
