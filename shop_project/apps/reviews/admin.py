from django.contrib import admin
from .models import Review

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
