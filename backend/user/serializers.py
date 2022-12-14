from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from user.models import User


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.refresh = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.refresh).blacklist()

        except TokenError:
            self.fail('Bad Token')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'lastname', 'username',
                  'password', 'email', 'rol', 'is_superuser')
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True},
            'is_superuser': {'read_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            name=validated_data['name'],
            lastname=validated_data['lastname'],
            is_superuser=validated_data['is_superuser'],
            rol=validated_data['rol'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        if validated_data.get('username'):
            instance.username = validated_data['username']
        if validated_data.get('name'):
            instance.name = validated_data['name']
        if validated_data.get('lastname'):
            instance.lastname = validated_data['lastname']
        if validated_data.get('is_superuser'):
            instance.is_superuser = validated_data['is_superuser']
        if validated_data.get('rol'):
            instance.role = validated_data['rol']
        if validated_data.get('password'):
            instance.set_password(validated_data['password'])
        instance.save()
        return instance
