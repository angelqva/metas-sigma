from rest_framework import serializers
from cliente.models import *


class EquipoClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Equipo
        fields = ('id', 'nombre', 'marca')
        extra_kwargs = {
            'id': {'read_only': True},
        }


class ClienteSerializer(serializers.ModelSerializer):
    equipos = EquipoClienteSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Cliente
        fields = ('id', 'name', 'lastname', 'username',
                  'password', 'email', 'rol', 'carnet_identidad', 'direccion', 'telefono', 'equipos')
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True},
            'rol': {'read_only': True},
        }


class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = '__all__'


class ResponsableReaderClienteEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsable
        fields = ('id', 'name', 'lastname', 'username',
                  'password', 'email', 'carnet_identidad', 'direccion', 'telefono')
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True},
        }


class ClienteEmpresaSerializer(serializers.ModelSerializer):
    responsables = ResponsableReaderClienteEmpresaSerializer(
        many=True, read_only=True, required=False)

    class Meta:
        model = ClienteEmpresa
        fields = ('id', 'name', 'lastname', 'username', 'password', 'email',
                  'rol', 'carnet_identidad', 'direccion', 'telefono',
                  'nombre_empresa', 'direccion_empresa', 'registro_empresa',
                  'telefono_empresa', 'responsables')
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True},
            'rol': {'read_only': True},
        }


class ResponsableSerializer(serializers.ModelSerializer):
    empresa = serializers.PrimaryKeyRelatedField(
        many=False, read_only=False, queryset=ClienteEmpresa.objects.all())

    class Meta:
        model = Responsable
        fields = ('id', 'name', 'lastname', 'username',
                  'password', 'email', 'rol', 'carnet_identidad', 'direccion', 'telefono', 'empresa')
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True},
            'rol': {'read_only': True},
        }
