from rest_framework import serializers

from .models import (
    Cliente,
    Equipo
)


class EquipoSerializers(serializers.ModelSerializer):
    cliente = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Equipo
        fields = ('id', 'nombre', 'marca', 'ubicacion', 'cliente')
        extra_kwargs = {
            'id': {'read_only': True},
        }

    def create(self, validated_data):
        kwargs: dict = self.context["view"].kwargs
        cliente_id = kwargs['cliente_pk']
        cliente = Cliente.objects.get(pk=cliente_id)
        validated_data["cliente"] = cliente
        return Equipo.objects.create(**validated_data)


class ClienteEquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = ('id', 'nombre', 'marca', 'ubicacion')
        extra_kwargs = {
            'id': {'read_only': True},
        }


class ClienteSerializer(serializers.ModelSerializer):
    equipos = ClienteEquipoSerializer(many=True, read_only=True)

    class Meta:
        model = Cliente
        fields = ('id', 'name', 'lastname', 'username', 'password', 'email', 'rol',
                  'carnet_identidad', 'direccion', 'telefono', 'equipos')
        extra_kwargs = {
          'id': {'read_only': True},
          'password': {'write_only': True},
          'rol': {'read_only': True},
        }
