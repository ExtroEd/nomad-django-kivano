from django.urls import path
from .views import (TokenObtainPairViewCustom, TokenRefreshViewCustom,
                    ProtectedView)


urlpatterns = [
    path('api/token/', TokenObtainPairViewCustom.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshViewCustom.as_view(),
         name='token_refresh'),
    path('protected/', ProtectedView.as_view(),
         name='protected_resource'),
]
