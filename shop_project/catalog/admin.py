from django.contrib import admin
from .models import Product, Review
from django import forms
from ckeditor.widgets import CKEditorWidget
from django.utils.translation import gettext_lazy as _


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'description': CKEditorWidget(),
        }


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductForm

    list_display = (
        'id',
        'name',
        'about',
        'price',
        'availability',
        'free_delivery',
        'description',
        'article',
        'created_at',
        'warranty',
    )
    list_filter = (
        'availability',
        'free_delivery',
        'category',
    )
    search_fields = (
        'name',
        'article',
        'category',
    )
    ordering = ('-created_at',)
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
        'article',
    )

    # Локализация заголовков секций
    fieldsets = (
        (None, {
            'fields': (
                'name',
                'about',
                'price',
                'availability',
                'category',
                'free_delivery',
            ),
        }),
        (_('Описание'), {
            'fields': ('description', 'warranty'),
        }),
        (_('Дополнительные данные'), {
            'fields': ('article', 'likes', 'reviews_count'),
        }),
        (_('Даты'), {
            'fields': ('created_at', 'updated_at'),
        }),
    )
    filter_horizontal = ()
    list_editable = (
        'price',
        'availability',
        'name',
        'about',
        'description',
        'warranty',
        'free_delivery',
    )
    date_hierarchy = 'created_at'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'name',
        'created_at',
    )
    search_fields = (
        'name',
        'product__name',
    )
