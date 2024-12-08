from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from catalog.views import home


schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="API for the Kivano store",
        terms_of_service="https://www.kivano.kg/privacy-policy",
        contact=openapi.Contact(email="feedback@kivano.kg"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('catalog.urls')),
    path('api/auth/', include('authentication.urls')),
    path('', home),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='swagger_ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='redoc_ui'),
]
