from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'cart', 'created_at']
    list_filter = ['created_at']
    search_fields = ['cart__user__username']
