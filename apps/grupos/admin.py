from django.contrib import admin
from .models import Grupo

@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cod', 'user', 'ativo',)

    list_filter = ('nome', 'cod', 'inclusao', 'user', 'ativo',)

    search_fields = ('nome', 'cod')