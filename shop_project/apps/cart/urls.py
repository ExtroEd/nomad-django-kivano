from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartViewSet, CartItemViewSet


router = DefaultRouter()
router.register('carts', CartViewSet)
router.register('cart-items', CartItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
