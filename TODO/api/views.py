from rest_framework import viewsets, status # viewsets são ótimos para APIs CRUD padrão
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Tarefa
from .serializers import TarefaSerializer

class TarefaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para visualizar e editar instâncias de Tarefa.
    """
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer

    @action(detail=True, methods=['post'], url_path='marcar-concluida')
    def marcar_concluida(self, request, pk=None):
        tarefa = self.get_object()
        tarefa.concluida = True
        tarefa.save()
        serializer = self.get_serializer(tarefa)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], url_path='marcar-nao-concluida')
    def marcar_nao_concluida(self, request, pk=None):
        tarefa = self.get_object()
        tarefa.concluida = False
        tarefa.save()
        serializer = self.get_serializer(tarefa)
        return Response(serializer.data, status=status.HTTP_200_OK)