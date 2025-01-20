from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderSerializer


class CreateOrderView(APIView):
    @extend_schema(
        request=OrderSerializer,
        responses={
            201: OrderSerializer,
            400: {
                'description': 'Bad Request',
                'content': {
                    'application/json': {
                        'example': {'detail': 'Invalid input data'}
                    }
                }
            }
        },
        description="Создаёт заказ на основе данных корзины.",
        summary="Создание заказа",
        tags=["Заказ"]
    )
    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
