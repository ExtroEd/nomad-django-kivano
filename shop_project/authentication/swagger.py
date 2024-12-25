from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.utils.translation import gettext_lazy as _


swagger_security = openapi.Parameter(
    'Authorization',
    openapi.IN_HEADER,
    description=_("Enter the token in the format: Bearer <your_token>"),
    type=openapi.TYPE_STRING,
)

schema_view = get_schema_view(
    openapi.Info(
        title=_("API Documentation"),
        default_version='v1',
        description=_("API for online store Kivano"),
        terms_of_service="https://www.kivano.kg/privacy-policy",
        contact=openapi.Contact(email="feedback@kivano.kg"),
        license=openapi.License(name=_("BSD License")),
        security=[
            {
                'Authorization': []
            }
        ],
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    authentication_classes=[],
)
