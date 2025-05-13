from django.contrib import admin
from .models import Tarefa

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'concluida', 'data_criacao', 'data_atualizacao')
    list_filter = ('concluida', 'data_criacao')
    search_fields = ('titulo', 'descricao')
