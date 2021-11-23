from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class AcordoAereoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'user', 'ativo',)

    list_filter = ('codigo', 'nome', 'user', 'inclusao', 'ativo',)

    search_fields = ('codigo', 'nome',)
