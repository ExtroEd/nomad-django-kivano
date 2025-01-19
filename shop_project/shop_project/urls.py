from apps.catalog.views import (home, GetCategoriesView, GetSubcategoriesView,
                                GetSubSubcategoriesView)
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from apps.catalog import views


urlpatterns = [
    path('api/catalog/', include('apps.catalog.urls')),
    path('api/reviews/', include('apps.reviews.urls')),
    path('api/cart/', include('apps.cart.urls')),
    path('api/users/', include('apps.users.urls')),

    # Swagger и схема API
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),

    path('auth/', include('apps.authentication.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('i18n/', include('django.conf.urls.i18n')),

    # Главная страница и категории
    path('', home, name='home'),
    path('categories/', GetCategoriesView.as_view(), name='get_categories'),
    path('categories/subcategories/', GetSubcategoriesView.as_view(),
         name='get_subcategories'),
    path('categories/subsubcategories/', GetSubSubcategoriesView.as_view(),
         name='get_subsubcategories'),
    path('product/<int:product_id>/like/', views.toggle_like,
         name='toggle_like'),

    # Административные маршруты
    path('admin/get_subcategories/', views.get_subcategories,
         name='get_subcategories'),
    path('admin/get_subsubcategories/', views.get_subsubcategories,
         name='get_subsubcategories'),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
