from rest_framework import serializers
from empresa.models import ClienteEmpresa, Responsable
from cliente.serializers import EquipoSerializers


class ResponsableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsable
        fields = ('id', 'name', 'lastname', 'username', 'password', 'email', 'rol',
                  'carnet_identidad', 'direccion', 'telefono', 'equipos', 'empresa')
        extra_kwargs = {
            'id': {'read_only': True},
            'rol': {'read_only': True},
        }

    empresa = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    equipos = EquipoSerializers(many=True, read_only=True)

    def create(self, validated_data):
        kwargs: dict = self.context["view"].kwargs
        empresa_pk = kwargs['empresa_pk']
        empresa = ClienteEmpresa.objects.get(pk=empresa_pk)
        validated_data["empresa"] = empresa
        return Responsable.objects.create(**validated_data)


class EmpresaResponsableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsable
        fields = ('id', 'name', 'lastname', 'username', 'password', 'email', 'rol',
                  'carnet_identidad', 'direccion', 'telefono', 'equipos')
        extra_kwargs = {
            'id': {'read_only': True},
            'rol': {'read_only': True},
        }

    equipos = EquipoSerializers(many=True, read_only=True)


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClienteEmpresa
        fields = ('id', 'name', 'lastname', 'username', 'password', 'email', 'rol',
                  'nombre_empresa', 'direccion_empresa', 'registro_empresa',
                  'telefono_empresa', 'responsables')
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True},
            'rol': {'read_only': True},
        }

    responsables = EmpresaResponsableSerializer(many=True, read_only=True)
