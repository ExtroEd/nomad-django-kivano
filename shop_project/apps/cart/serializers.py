from rest_framework import serializers
from .models import Cart, CartItem
from apps.catalog.models import Product


class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_price = serializers.FloatField(source='product.price',
                                           read_only=True)
    total_price = serializers.FloatField(read_only=True)


    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product', 'product_name', 'product_price',
                  'quantity', 'total_price']


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, read_only=True)
    total_items = serializers.IntegerField(read_only=True)
    total_price = serializers.FloatField(read_only=True)


    class Meta:
        model = Cart
        fields = ['id', 'user', 'session_key', 'created_at', 'cart_items',
                  'total_items', 'total_price']
