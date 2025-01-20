from rest_framework import serializers
from apps.cart.models import Cart, CartItem
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['id', 'created_at']

    def create(self, validated_data):
        cart = validated_data['cart']
        if cart.cart_items.count() == 0:
            raise serializers.ValidationError("Корзина пуста.")

        order = super().create(validated_data)
        cart.cart_items.all().delete()
        return order
