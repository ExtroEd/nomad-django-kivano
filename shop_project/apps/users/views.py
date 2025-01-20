from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import CustomUser
from .serializers import (RegistrationSerializer, LoginSerializer,
                          CustomUserSerializer)


class RegisterView(APIView):
    serializer_class = RegistrationSerializer

    @extend_schema(
        summary="Регистрация нового пользователя",
        description=(
            "Позволяет зарегистрировать нового пользователя. "
            "Для регистрации отправьте данные, такие как имя, email и пароль. "
            "В случае успеха возвращает ID созданного пользователя."
        ),
        tags=['Пользователи'],
        request=RegistrationSerializer,
        responses={
            201: OpenApiResponse(
                description="Регистрация успешна. Возвращается ID нового пользователя."
            ),
            400: OpenApiResponse(
                description="Некорректные данные. Проверьте заполненность и корректность полей."
            )
        }
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "Регистрация успешна",
                "user_id": user.id
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    @extend_schema(
        summary="Авторизация пользователя",
        description=(
            "Позволяет авторизоваться пользователю с использованием email и "
            "пароля. Возвращает пару токенов: access и refresh. В случае "
            "некорректных данных возвращает сообщение об ошибке."
        ),
        tags=['Пользователи'],
        request=LoginSerializer,
        responses={
            200: OpenApiResponse(
                description="Авторизация успешна. Возвращается пара токенов."
            ),
            401: OpenApiResponse(
                description="Ошибка авторизации. Некорректные данные."
            )
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UserListView(APIView):
    serializer_class = CustomUserSerializer

    class UserPagination(PageNumberPagination):
        page_size = 10

    @extend_schema(
        summary="Список пользователей с пагинацией",
        description=(
            "Возвращает список пользователей с поддержкой пагинации. Каждая "
            "страница содержит фиксированное количество записей (по умолчанию "
            "10). Если пользователей нет, возвращается сообщение с "
            "соответствующим статусом."
        ),
        tags=['Пользователи'],
        responses={
            200: CustomUserSerializer(many=True),
            404: OpenApiResponse(
                description="Нет пользователей в системе."
            )
        }
    )
    def get(self, request):
        users = CustomUser.objects.all()
        if not users.exists():
            return Response({"message": "Нет пользователей"},
                            status=status.HTTP_404_NOT_FOUND)

        paginator = self.UserPagination()
        result_page = paginator.paginate_queryset(users, request)
        serializer = self.serializer_class(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
