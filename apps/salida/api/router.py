from rest_framework.routers import DefaultRouter
from apps.salida.api.views import SalidaViewSet

router_salida = DefaultRouter()
router_salida.register(prefix="salida", basename="salida", viewset= SalidaViewSet)