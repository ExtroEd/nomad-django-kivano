from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from catalog.views import home # Игнор
from authentication.swagger import schema_view # Игнор
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('api/', include('catalog.urls')),
    path('', home, name='home'),
    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='swagger_ui'
    ),
    path('swagger.json', schema_view.without_ui(cache_timeout=0),
         name='swagger_json'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='redoc_ui'),
    path('auth/', include('authentication.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
