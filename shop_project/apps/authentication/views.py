from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from drf_spectacular.utils import (extend_schema, OpenApiParameter,
                                   OpenApiResponse)
from django.shortcuts import render


class TokenObtainPairViewCustom(TokenObtainPairView):
    @extend_schema(
        summary="Получение токенов доступа",
        description=(
            "Позволяет получить пару токенов (access и refresh) для "
            "авторизации. Требуется отправить валидные учетные данные "
            "пользователя. Если данные корректны, возвращается пара токенов."
        ),
        tags=["Токены"],
        responses={
            200: OpenApiResponse(
                description="Успешная аутентификация. Возвращается пара "
                            "токенов."
            ),
            401: OpenApiResponse(
                description="Ошибка авторизации. Неверные учетные данные."
            )
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class TokenRefreshViewCustom(TokenRefreshView):
    @extend_schema(
        summary="Обновление токена доступа",
        description=(
            "Позволяет обновить токен доступа (access token), используя "
            "refresh токен. Для этого в запросе необходимо предоставить "
            "refresh токен. Возвращает новый токен доступа."
        ),
        tags=["Токены"],
        responses={
            200: OpenApiResponse(
                description="Успешное обновление. Возвращается новый токен "
                            "доступа."
            ),
            401: OpenApiResponse(
                description="Ошибка авторизации. Неверный или истекший "
                            "refresh токен."
            )
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Доступ к защищенному ресурсу",
        description=(
            "Позволяет получить доступ к защищенному ресурсу. Для доступа "
            "необходимо предоставить валидный токен авторизации в заголовке "
            "`Authorization` с префиксом `Bearer`."
        ),
        tags=["Токены"],
        parameters=[
            OpenApiParameter(
                name='Authorization',
                required=True,
                type=str,
                location=OpenApiParameter.HEADER,
                description="Токен авторизации в формате `Bearer <token>`."
            ),
        ],
        responses={
            200: OpenApiResponse(
                description="Доступ разрешен. Возвращается сообщение о "
                            "защищенном ресурсе."
            ),
            401: OpenApiResponse(
                description="Ошибка авторизации. Необходимо предоставить "
                            "валидный токен."
            )
        }
    )
    def get(self, request):
        return Response({"message": "You have successfully gained access to "
                                    "the protected resource."})
