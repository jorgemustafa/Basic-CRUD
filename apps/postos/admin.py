from django.contrib import admin
from .models import POS

@admin.register(POS)
class POSAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'user', 'ativo',)

    list_filter = ('codigo', 'nome', 'inclusao', 'user', 'ativo',)

    search_fields = ('codigo', 'nome',)