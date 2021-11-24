from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Colaborador

@admin.register(Colaborador)
class ColaboradorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nome', 'email', 'user', 'ativo')

    list_filter = ('nome', 'email', 'inclusao', 'user', 'ativo',)

    search_fields = ('nome', 'email',)

    readonly_fields = ('inclusao', 'edicao',)

