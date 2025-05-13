from django.db import models
import uuid # Para um ID único, se preferir em vez do ID padrão do Django

class Tarefa(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) # ID UUID Opcional
    titulo = models.CharField(max_length=200, verbose_name="Título")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    concluida = models.BooleanField(default=False, verbose_name="Concluída?")
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-data_criacao'] # Sort the tasks
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"