from django.db import models
from django.core.validators import RegexValidator
from user.models import *



class Cliente(User):
    carnet_identidad = models.CharField(unique=True, max_length=11, validators=[
        RegexValidator(
            r"^[0-9]*$", "Solo aceptan digitos")
    ])
    direccion = models.TextField(blank=False)
    telefono = models.CharField(blank=True, max_length=15)

    def __str__(self):
        return f"Cliente({self.username})"

class Equipo(models.Model):
    cliente = models.ForeignKey(Cliente, related_name="equipos", on_delete=models.CASCADE)
    nombre = models.CharField(blank=False, null=False, max_length=50)
    marca = models.CharField(blank=False, null=False, max_length=50)
    ubicacion = models.CharField(blank=False, null=False, max_length=100)

class ClienteEmpresa(Cliente):
    nombre_empresa = models.CharField(unique=True, max_length=100, blank=False)
    direccion_empresa = models.TextField(blank=False)
    registro_empresa = models.CharField(
        unique=True, max_length=100, blank=False)
    telefono_empresa = models.CharField(blank=True, max_length=15)

    def __str__(self):
        return f"Empresa:[cliente:({self.username}), empresa({self.nombre_empresa})]"


class Responsable(Cliente):
    empresa = models.ForeignKey(
        ClienteEmpresa, related_name="responsables", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Responsable:({self.username})"
