from django.forms import ValidationError
from rest_framework import status, viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from cliente.serializers import *
from rest_framework_simplejwt.tokens import TokenError
from django.core.exceptions import PermissionDenied
from typing import *


class ClienteView(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Cliente.objects.all().prefetch_related('equipos').all()

    @action(detail=True, url_path="equipos", methods=["post"],
            serializer_class=EquipoClienteSerializer)
    def equipos_create(self, request, **kwargs):
        cliente: Cliente = self.get_object()
        request.data["cliente"] = cliente
        equipo_serializer = EquipoClienteSerializer(
            data=request.data)
        equipo_serializer.is_valid(raise_exception=True)
        instance = equipo_serializer.save()
        # cliente.equipos.add(instance)
        return Response(equipo_serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, url_path="equipos/<id>", methods=["put"],
            serializer_class=EquipoClienteSerializer)
    def equipos_update(self, request, **kwargs):
        print("update Equipo request", request)
        print("update Equipo kwargs", kwargs)
        return Response({"response": True}, status=status.HTTP_200_OK)

    @action(detail=True, url_path="equipos/<id>", methods=["delete"],
            serializer_class=EquipoClienteSerializer)
    def equipos_delete(self, request, **kwargs):
        print("delete Equipo request", request)
        print("delete Equipo kwargs", kwargs)
        return Response({"response": True}, status=status.HTTP_200_OK)


class ClienteEmpresaView(viewsets.ModelViewSet):
    serializer_class = ClienteEmpresaSerializer
    permission_classes = (IsAuthenticated,)
    queryset = ClienteEmpresa.objects.all().prefetch_related('responsables').all()

    @action(detail=True, url_path="nuevo-responsable", methods=["post"],
            serializer_class=ResponsableReaderClienteEmpresaSerializer)
    def nuevo_responsable(self, request, **kwargs):
        empresa: ClienteEmpresa = self.get_object()
        request.data["empresa"] = empresa
        responsable_serializer = ResponsableReaderClienteEmpresaSerializer(
            data=request.data)
        responsable_serializer.is_valid(raise_exception=True)
        instance = responsable_serializer.save()
        # empresa.responsables.add(instance)
        return Response(responsable_serializer.data, status=status.HTTP_200_OK)
