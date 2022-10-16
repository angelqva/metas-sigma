from rest_framework import status, viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from user.serializers import *
from rest_framework_simplejwt.tokens import TokenError
from django.core.exceptions import PermissionDenied
from typing import *


class LogoutView(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = LogoutSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        success = True
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except TokenError:
            success = False

        return Response({'success': success}, status=status.HTTP_200_OK)


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        user: User = self.request.user
        if user.is_superuser:
            return super().create(request, *args, **kwargs)
        else:
            raise PermissionDenied()

    def update(self, request, *args, **kwargs):
        user: User = self.request.user
        if user.is_superuser:
            return super().update(request, *args, **kwargs)
        else:
            raise PermissionDenied()

    def partial_update(self, request, *args, **kwargs):
        user: User = self.request.user
        if user.is_superuser:
            return super().partial_update(request, *args, **kwargs)
        else:
            raise PermissionDenied()

    def destroy(self, request, *args, **kwargs):
        user: User = self.request.user
        if user.is_superuser:
            return super().destroy(request, *args, **kwargs)
        else:
            raise PermissionDenied()

    def list(self, request, *args, **kwargs):
        user: User = self.request.user
        if user.is_superuser:
            return super().list(request, *args, **kwargs)
        else:
            raise PermissionDenied()

    @action(detail=False, methods=["get"])
    def me(self, request):
        user: User = self.request.user
        read = UserSerializer(user)
        return Response(read.data, status=status.HTTP_200_OK)
