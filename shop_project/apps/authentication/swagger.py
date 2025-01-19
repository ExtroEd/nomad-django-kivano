from rest_framework import permissions
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.utils.translation import gettext_lazy as _


schema_view = SpectacularSwaggerView.as_view(
    url_name='schema',
    public=True
)

schema_view_with_api = SpectacularAPIView.as_view()
