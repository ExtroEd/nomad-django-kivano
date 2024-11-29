from rest_framework import serializers
from .models import Product


def validate_article(value):
    if Product.objects.filter(article=value).exists():
        raise serializers.ValidationError(
            "Product with this article already exists.")
    return value


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

