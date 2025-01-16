from authentication.swagger import schema_view
from catalog import urls as catalog_urls
from catalog.views import home
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from catalog import views


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
    path('', include(catalog_urls)),
    path('admin/get_subcategories/', views.get_subcategories, name='get_subcategories'),
    path('admin/get_subsubcategories/', views.get_subsubcategories, name='get_subsubcategories'),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
