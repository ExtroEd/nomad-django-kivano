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
        tags=['Пользователи'],
        description="Регистрация нового пользователя. Для регистрации нового "
                    "пользователя отправьте необходимые данные (имя, email, "
                    "пароль) в запросе.",
        request=RegistrationSerializer,
        responses={
            201: OpenApiResponse(
                description="Регистрация успешна. Возвращается ID нового "
                            "пользователя."),
            400: OpenApiResponse(
                description="Некорректные данные. Пожалуйста, убедитесь, что "
                            "все поля корректны и соответствуют требованиям.")
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

    @extend_schema(tags=['Пользователи'])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UserListView(APIView):
    serializer_class = CustomUserSerializer

    class UserPagination(PageNumberPagination):
        page_size = 10

    @extend_schema(
        tags=['Пользователи'],
        description="Получение списка пользователей с пагинацией",
        responses={
            200: CustomUserSerializer(many=True),
            404: OpenApiResponse(description="Нет пользователей")
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
