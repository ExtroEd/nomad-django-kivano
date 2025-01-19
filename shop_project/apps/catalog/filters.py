import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    # Пример фильтра по имени
    name = django_filters.CharFilter(lookup_expr='icontains',
                                     label='Product Name')

    # Фильтр по цене, например
    price_min = django_filters.NumberFilter(field_name='price',
                                            lookup_expr='gte',
                                            label='Min Price')
    price_max = django_filters.NumberFilter(field_name='price',
                                            lookup_expr='lte',
                                            label='Max Price')

    # Фильтр по категории
    category = django_filters.CharFilter(lookup_expr='icontains',
                                         label='Category')

    class Meta:
        model = Product
        fields = ['name', 'price_min', 'price_max', 'category']
