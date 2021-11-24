from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Fee


@admin.register(Fee)
class FeeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('cliente', 'renovacao', 'user', 'ativo',)

    list_filter = ('cliente', 'user', 'ativo',)

    search_fields = ('cliente', 'renovacao',)

    readonly_fields = ('inclusao', 'edicao',)


