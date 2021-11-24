from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Produto

@admin.register(Produto)
class AcordoAereoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'user', 'ativo',)

    list_filter = ('codigo', 'nome', 'user', 'inclusao', 'ativo',)

    search_fields = ('codigo', 'nome',)

    readonly_fields = ('inclusao', 'edicao',)

