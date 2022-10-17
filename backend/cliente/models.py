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
