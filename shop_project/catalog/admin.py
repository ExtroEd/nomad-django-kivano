from django.contrib import admin
from .models import Product, Review
from django import forms
from ckeditor.widgets import CKEditorWidget


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'  # Или укажите конкретные поля, если нужно
        widgets = {
            'description': CKEditorWidget(),  # Используем CKEditor для поля description
        }


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductForm  # Указываем форму с CKEditor

    list_display = ('id', 'name', 'about', 'price', 'availability',
                    'free_delivery', 'description', 'article', 'created_at',
                    'warranty')
    list_filter = ('availability', 'free_delivery', 'category')
    search_fields = ('name', 'article', 'category')
    ordering = ('-created_at',)
    readonly_fields = (
        'id', 'created_at', 'updated_at', 'article')  # Не редактируемые поля
    fieldsets = (
        (None, {
            'fields': ('name', 'about', 'price', 'availability', 'category',
                       'free_delivery')  # Основная информация
        }),
        ('Описание', {
            'fields': ('description', 'warranty')  # Дополнительное описание и гарантия
        }),
        ('Дополнительные данные', {
            'fields': ('article', 'likes', 'reviews_count')  # Артикул и другие данные
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at')  # Даты
        }),
    )
    filter_horizontal = ()
    list_editable = (
        'price', 'availability', 'name', 'about', 'description', 'warranty',
        'free_delivery')  # Все редактируемые поля
    date_hierarchy = 'created_at'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'name', 'created_at')
    search_fields = ('name', 'product__name')
