from django.contrib import admin
from RevenueExpenseControl.models import *


class ReceitasAdmin(admin.ModelAdmin):
    list_display = ('id', 'valor', 'data', 'descricao')
    list_display_links = ('descricao',)
    list_per_page = 10

admin.site.register(Receita, ReceitasAdmin)


class DespesasAdmin(admin.ModelAdmin):
    list_display = ('id', 'valor', 'data', 'descricao', 'categoria')
    list_display_links = ('descricao',)
    list_editable = ('categoria',)
    list_per_page = 10

admin.site.register(Despesa, DespesasAdmin)