from rest_framework import serializers
from .models import Tarefa

class TarefaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        # fields = '__all__' # Include all fields
        fields = ['id', 'titulo', 'descricao', 'concluida', 'data_criacao', 'data_atualizacao']
        read_only_fields = ['data_criacao', 'data_atualizacao'] # Not direct editable fields by API