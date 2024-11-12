from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from django.http import HttpResponse


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def home(request):
    return HttpResponse("Добро пожаловать на главную страницу!")
