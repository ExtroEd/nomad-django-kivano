import logging
import requests
from django.conf import settings
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Review
from .serializers import ReviewSerializer


logger = logging.getLogger(__name__)


def verify_recaptcha(recaptcha_response):
    recaptcha_verify_url = 'https://www.google.com/recaptcha/api/siteverify'
    recaptcha_data = {
        'secret': settings.RECAPTCHA_PRIVATE_KEY,
        'response': recaptcha_response,
    }
    try:
        response = requests.post(recaptcha_verify_url, data=recaptcha_data)
        response_json = response.json()
        return response_json.get('success', False), response_json
    except requests.RequestException as e:
        logger.error(f"Error during reCAPTCHA verification: {e}")
        return False, None


@extend_schema(tags=["Отзывы"])  # Применяем теги ко всему классу
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    @extend_schema(description="Получение списка всех отзывов")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(description="Получение отзыва по ID")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(description="Обновление отзыва")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(description="Удаление отзыва")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @extend_schema(description="Частичное обновление отзыва")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(description="Создание нового отзыва")
    def create(self, request, *args, **kwargs):
        recaptcha_response = request.data.get('g-recaptcha-response')
        if not recaptcha_response:
            return Response(
                {"error": "reCAPTCHA response is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        is_valid, recaptcha_result_json = verify_recaptcha(recaptcha_response)
        if not is_valid:
            logger.warning(f"Invalid reCAPTCHA: {recaptcha_result_json}")
            return Response(
                {"error": "Invalid reCAPTCHA. Please try again."},
                status=status.HTTP_400_BAD_REQUEST
            )

        return super().create(request, *args, **kwargs)
