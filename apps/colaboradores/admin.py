from django.contrib import admin
from .models import Colaborador

@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'user', 'ativo')

    list_filter = ('nome', 'email', 'inclusao', 'user', 'ativo',)

    search_fields = ('nome', 'email',)

