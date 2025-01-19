from apps.authentication.swagger import schema_view
from apps.catalog import views
from apps.catalog.views import (home, GetCategoriesView, GetSubcategoriesView,
                                GetSubSubcategoriesView)
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('api/', include('apps.catalog.urls')),
    path('api/', include('apps.reviews.urls')),
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
    path('auth/', include('apps.authentication.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('categories/', GetCategoriesView.as_view(), name='get_categories'),
    path('categories/subcategories/', GetSubcategoriesView.as_view(),
         name='get_subcategories'),
    path('categories/subsubcategories/', GetSubSubcategoriesView.as_view(),
         name='get_subsubcategories'),
    path('product/<int:product_id>/like/', views.toggle_like,
         name='toggle_like'),
    path('admin/get_subcategories/', views.get_subcategories,
         name='get_subcategories'),
    path('admin/get_subsubcategories/', views.get_subsubcategories,
         name='get_subsubcategories'),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
