from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from drf_spectacular.utils import (extend_schema, OpenApiParameter,
                                   OpenApiResponse)
from django.shortcuts import render


class TokenObtainPairViewCustom(TokenObtainPairView):
    @extend_schema(tags=["Токены"])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class TokenRefreshViewCustom(TokenRefreshView):
    @extend_schema(tags=["Токены"])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=["Токены"],
        description="Доступ к защищенному ресурсу. Для доступа к этому "
                    "эндпоинту, пожалуйста, используйте валидный токен "
                    "авторизации.",
        parameters=[
            OpenApiParameter(
                name='Authorization',
                required=True,
                type=str,
                location=OpenApiParameter.HEADER,
                description="Bearer token for authorization"
            ),
        ],
        responses={
            200: OpenApiResponse(
                description="Доступ разрешен. Возвращает сообщение о "
                            "защищенном ресурсе."),
            401: OpenApiResponse(
                description="Ошибка авторизации. Пожалуйста, предоставьте "
                            "действующий токен.")
        }
    )
    def get(self, request):
        return Response({"message": "You have successfully gained access to "
                                    "the protected resource."})
