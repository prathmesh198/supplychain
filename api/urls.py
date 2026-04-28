from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, SupplierViewSet, ShipmentViewSet, RouteViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'shipments', ShipmentViewSet)
router.register(r'routes', RouteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
