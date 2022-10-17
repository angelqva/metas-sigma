from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers

from empresa import views

empresa_router = SimpleRouter()
empresa_router.register('empresas', views.EmpresaView, basename='empresas')

responsable_router = routers.NestedSimpleRouter(
    empresa_router,
    r'empresas',
    lookup='empresa')

responsable_router.register(
    r'responsables',
    views.ResponsableView,
    basename='responsables'
)
