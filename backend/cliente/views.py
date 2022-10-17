from rest_framework import viewsets
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from cliente.serializers import *


class ClienteView(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Cliente.objects.all().prefetch_related('equipos')


class EquipoView(viewsets.ModelViewSet):
    queryset = Equipo.objects.all().select_related(
        'cliente'
    )
    serializer_class = EquipoSerializers
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, *args, **kwargs):
        cliente_id = self.kwargs.get("cliente_pk")
        try:
            cliente = Cliente.objects.get(pk=cliente_id)
        except Cliente.DoesNotExist:
            raise NotFound('Cliente not found')
        return self.queryset.filter(cliente=cliente)
