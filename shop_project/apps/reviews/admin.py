from django.contrib import admin
from .models import Review
from apps.catalog.models import Product


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'created_at')
    list_filter = ('product', 'created_at')
    search_fields = ('name', 'comment', 'product__name')
    readonly_fields = ('created_at',)
    fieldsets = (
        (None, {
            'fields': ('product', 'name', 'comment')
        }),
        ('Timestamps', {
            'fields': ('created_at',)
        }),
    )

    def save_model(self, request, obj, form, change):
        """
        Пересчитывает количество отзывов при сохранении нового отзыва.
        """
        super().save_model(request, obj, form, change)
        product = obj.product
        product.reviews_count = product.reviews.count()
        product.save()

    def delete_model(self, request, obj):
        """
        Пересчитывает количество отзывов при удалении отзыва.
        """
        product = obj.product
        super().delete_model(request, obj)
        product.reviews_count = product.reviews.count()
        product.save()
