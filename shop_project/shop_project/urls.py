from django.contrib import admin
from django.urls import path, include
from catalog.views import home
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="API Decumentation",
        default_version='v1',
        description="API for the Kivano store",
        terms_of_service="https://www.kivano.kg/terms",
        contact=openapi.Contact(email="contact@kivano.kg"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('catalog.urls')),
    path('', home),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='swagger_ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='redoc_ui'),
]
