from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static
from cliente.urls import router as cliente_router, equipo_router
from empresa.urls import empresa_router, responsable_router

schema_view = get_schema_view(
    openapi.Info(
        title="METAS-SIGMA APIREST",
        default_version='v1',
        description="Django, DjangoRestFramework, Postgres, SimpleJWT",
        terms_of_service="https://github.com/angelqva/metas-sigma",
        contact=openapi.Contact(email="angel.napolesqva@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(cliente_router.urls)),
    path('api/', include(equipo_router.urls)),
    path('api/', include(empresa_router.urls)),
    path('api/', include(responsable_router.urls)),
    path('api/login/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui(
        'redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
