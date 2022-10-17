from rest_framework import viewsets
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from empresa.serializers import *


class EmpresaView(viewsets.ModelViewSet):
    serializer_class = EmpresaSerializer
    permission_classes = (IsAuthenticated,)
    queryset = ClienteEmpresa.objects.all().prefetch_related(
        'responsables', 'responsables__equipos'
    )


class ResponsableView(viewsets.ModelViewSet):
    queryset = Responsable.objects.all().select_related(
        'empresa'
    ).prefetch_related('equipos')
    serializer_class = ResponsableSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, *args, **kwargs):
        empresa_id = self.kwargs.get("empresa_pk")
        try:
            empresa = ClienteEmpresa.objects.get(pk=empresa_id)
        except ClienteEmpresa.DoesNotExist:
            raise NotFound('Empresa not found')
        return self.queryset.filter(empresa=empresa)
