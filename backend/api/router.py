from rest_framework.routers import DefaultRouter
from user.views import *
from cliente.views import *

router = DefaultRouter()
router.register(prefix='users', basename='users', viewset=UserView)
router.register(prefix='logout', basename='logout', viewset=LogoutView)
router.register(prefix='clientes', basename='clientes', viewset=ClienteView)
router.register(prefix='empresas', basename='empresas',
                viewset=ClienteEmpresaView)
