from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers

from cliente import views

router = SimpleRouter()
router.register('clientes', views.ClienteView)

equipo_router = routers.NestedSimpleRouter(
    router,
    r'clientes',
    lookup='cliente')

equipo_router.register(
    r'equipos',
    views.EquipoView,
    basename='equipos'
)
