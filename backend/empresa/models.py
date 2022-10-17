from django.db import models
from user.models import User
from cliente.models import Cliente


class ClienteEmpresa(User):
    nombre_empresa = models.CharField(unique=True, max_length=100, blank=False)
    direccion_empresa = models.TextField(blank=False)
    registro_empresa = models.CharField(
        unique=True, max_length=100, blank=False)
    telefono_empresa = models.CharField(blank=True, max_length=15)

    def __str__(self):
        return f"Empresa:[cliente:({self.username}), empresa({self.nombre_empresa})]"


class Responsable(Cliente):
    empresa = models.ForeignKey(ClienteEmpresa, related_name="responsables", on_delete=models.CASCADE,
                                null=True, blank=True)

    def __str__(self):
        return f"Responsable:({self.username}, empresa({self.empresa.nombre_empresa}))"
