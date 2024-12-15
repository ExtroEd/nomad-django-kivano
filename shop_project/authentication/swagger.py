from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# Определение схемы безопасности с использованием API-ключа в заголовке
swagger_security = openapi.Parameter(
    'Authorization',  # Имя параметра
    openapi.IN_HEADER,  # Параметр в заголовке
    description="Введите токен в формате: Bearer <ваш_токен>",
    type=openapi.TYPE_STRING,
)

# Настройка схемы безопасности через get_schema_view
schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="API for the Kivano store",
        terms_of_service="https://www.kivano.kg/privacy-policy",
        contact=openapi.Contact(email="feedback@kivano.kg"),
        license=openapi.License(name="BSD License"),
        security=[  # Указываем здесь безопасность
            {
                'Authorization': []  # Это соответствует нашему заголовку
            }
        ],
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    authentication_classes=[],  # Убедитесь, что не добавляете тут свои классы авторизации
)
