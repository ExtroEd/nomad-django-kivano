from django.contrib import admin
from .models import Product, Category, SubCategory, SubSubCategory, Review
from django import forms
from ckeditor.widgets import CKEditorWidget
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'description': CKEditorWidget(),
        }

    def clean(self):
        cleaned_data = super().clean()
        # category = cleaned_data.get('category')
        # subcategory = cleaned_data.get('subcategory')
        # subsubcategory = cleaned_data.get('subsubcategory')
        #
        # if subcategory and subcategory.category != category:
        #     raise ValidationError({
        #         'subcategory': _('Выбранная подкатегория не соответствует категории.'),
        #     })
        #
        # if subsubcategory and subsubcategory.subcategory != subcategory:
        #     raise ValidationError({
        #         'subsubcategory': _('Выбранная под-подкатегория не соответствует подкатегории.'),
        #     })

        return cleaned_data


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
        'category',
        'subcategory',
        'subsubcategory',
        'created_at',
        'warranty',
    )
    list_filter = (
        'availability',
        'free_delivery',
        'category',
        'subcategory',
        'subsubcategory',
        'created_at',
    )
    search_fields = (
        'name',
        'article',
        'category__name',
        'subcategory__name',
        'subsubcategory__name',
    )
    ordering = ('-created_at',)
    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
        'article',
    )
    fieldsets = (
        (None, {
            'fields': (
                'name',
                'about',
                'price',
                'availability',
                'category',
                'subcategory',
                'subsubcategory',
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
    list_editable = (
        'price',
        'availability',
        'free_delivery',
    )
    date_hierarchy = 'created_at'

    class Media:
        js = ('admin/js/category_filter.js',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        obj = getattr(request, 'obj', None)

        if db_field.name == 'subcategory':
            if obj and obj.category:
                kwargs['queryset'] = SubCategory.objects.filter(
                    category=obj.category)
            else:
                kwargs[
                    'queryset'] = SubCategory.objects.all()  # Возвращаем все подкатегории, если категория не выбрана

        if db_field.name == 'subsubcategory':
            if obj and obj.subcategory:
                kwargs['queryset'] = SubSubCategory.objects.filter(
                    subcategory=obj.subcategory)
            else:
                kwargs[
                    'queryset'] = SubSubCategory.objects.all()  # Возвращаем все под-подкатегории, если подкатегория не выбрана

        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    list_filter = ('category',)


@admin.register(SubSubCategory)
class SubSubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subcategory')
    list_filter = ('subcategory',)


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
