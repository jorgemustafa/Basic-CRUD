from django.contrib import admin
from .models import Fee


@admin.register(Fee)
class FeeAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'renovacao', 'user', 'ativo',)

    list_filter = ('cliente', 'user', 'ativo',)

    search_fields = ('cliente', 'renovacao')
