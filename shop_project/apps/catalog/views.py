from apps.catalog.models import Category, SubCategory, SubSubCategory, Product
from django.http import JsonResponse
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import generics, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .filters import ProductFilter
from .models import Product, SubCategory, SubSubCategory, ProductLike
from .serializers import (ProductSerializer, ProductLikeSerializer,
                          LikeResponseSerializer)


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def home(request):
    products = Product.objects.all().order_by('-created_at')[:28]
    return render(request, 'home.html', {'products': products})


from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    renderer_classes = [JSONRenderer]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['name', 'description', 'category']
    ordering_fields = ['price', 'name']

    @extend_schema(
        summary="Получить список продуктов",
        description=(
            "Возвращает список всех доступных продуктов. "
            "Можно использовать фильтры, поиск и сортировку по следующим "
            "полям: `name`, `description`, `category`, `price`."
        ),
        tags=['Продукты']
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Создать новый продукт",
        description="Добавляет новый продукт в базу данных. Требуется указать "
                    "все обязательные поля.",
        tags=['Продукты']
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary="Получить продукт по ID",
        description="Возвращает данные продукта по указанному идентификатору "
                    "(ID).",
        tags=['Продукты']
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Обновить продукт полностью",
        description="Обновляет все поля продукта по указанному ID. Требуется "
                    "передать все поля.",
        tags=['Продукты']
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        summary="Обновить продукт частично",
        description="Частично обновляет поля продукта по указанному ID. Можно "
                    "указать только изменяемые поля.",
        tags=['Продукты']
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        summary="Удалить продукт",
        description="Удаляет продукт из базы данных по указанному ID.",
        tags=['Продукты']
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


def get_subcategories(request):
    category_id = request.GET.get('category_id')
    subcategories = (SubCategory.objects.filter(category_id=category_id)
                     .values('id', 'name'))
    return JsonResponse({'subcategories': list(subcategories)})


def get_subsubcategories(request):
    subcategory_id = request.GET.get('subcategory_id')
    subsubcategories = SubSubCategory.objects.filter(
        subcategory_id=subcategory_id).values('id', 'name')
    return JsonResponse({'subsubcategories': list(subsubcategories)})


class GetCategoriesView(APIView):
    @extend_schema(
        summary="Получить список категорий",
        description=(
            "Возвращает список всех категорий. Каждая категория содержит "
            "следующие поля: `id` (идентификатор категории) и `name` "
            "(название категории)."
        ),
        tags=["Категории"],
        responses={
            200: OpenApiTypes.OBJECT,
        },
    )
    def get(self, request):
        categories = Category.objects.all().values('id', 'name')
        return Response({"categories": list(categories)},
                        status=status.HTTP_200_OK)


class GetSubcategoriesView(APIView):
    @extend_schema(
        summary="Получить список подкатегорий",
        description=(
            "Возвращает список всех подкатегорий. Если указан параметр "
            "`category_id`, возвращаются только подкатегории, относящиеся к "
            "указанной категории. Каждая подкатегория содержит поля: `id`, "
            "`name`, и `category_id` (если фильтрация не используется)."
        ),
        tags=["Категории"],
        parameters=[
            OpenApiParameter(
                name="category_id",
                description="ID категории для фильтрации подкатегорий.",
                required=False,
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
            )
        ],
        responses={
            200: OpenApiTypes.OBJECT,
        },
    )
    def get(self, request):
        category_id = request.query_params.get('category_id')
        if category_id:
            subcategories = SubCategory.objects.filter(
                category_id=category_id).values('id', 'name')
        else:
            subcategories = SubCategory.objects.all().values(
                'id', 'name', 'category_id')

        return Response({"subcategories": list(subcategories)},
                        status=status.HTTP_200_OK)


class GetSubSubcategoriesView(APIView):
    @extend_schema(
        summary="Получить список под-подкатегорий",
        description=(
            "Возвращает список всех под-подкатегорий. Если указан параметр "
            "`subcategory_id`, возвращаются только под-подкатегории, "
            "относящиеся к указанной подкатегории. Каждая под-подкатегория "
            "содержит поля: `id`, `name`, и `subcategory_id` (если фильтрация "
            "не используется)."
        ),
        tags=["Категории"],
        parameters=[
            OpenApiParameter(
                name="subcategory_id",
                description="ID подкатегории для фильтрации под-подкатегорий.",
                required=False,
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
            )
        ],
        responses={
            200: OpenApiTypes.OBJECT,
        },
    )
    def get(self, request):
        subcategory_id = request.query_params.get('subcategory_id')
        if subcategory_id:
            subsubcategories = SubSubCategory.objects.filter(
                subcategory_id=subcategory_id).values('id', 'name')
        else:
            subsubcategories = (SubSubCategory.objects.all()
                                .values('id', 'name', 'subcategory_id'))

        return Response({"subsubcategories": list(subsubcategories)},
                        status=status.HTTP_200_OK)


@extend_schema(
    methods=['POST'],
    tags=["Лайки"],
    summary="Поставить лайк продукту",
    description="Добавляет лайк текущего пользователя к продукту. "
                "Возвращает подтверждение успешного добавления.",
    request=None,
    responses={201: LikeResponseSerializer}
)
@extend_schema(
    methods=['DELETE'],
    tags=["Лайки"],
    summary="Убрать лайк с продукта",
    description="Удаляет лайк текущего пользователя с продукта. "
                "Возвращает подтверждение успешного удаления.",
    request=None,
    responses={
        204: LikeResponseSerializer,
        400: LikeResponseSerializer
    }
)
@api_view(['POST', 'DELETE'])
def toggle_like(request, product_id):
    user = request.user
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response({"detail": "Product not found."},
                        status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        if ProductLike.objects.filter(user=user, product=product).exists():
            return Response({"detail": "You already liked this product."},
                            status=status.HTTP_400_BAD_REQUEST)

        ProductLike.objects.create(user=user, product=product)
        product.update_likes_count()
        return Response(LikeResponseSerializer({"detail": "Like added."}).data,
                        status=status.HTTP_201_CREATED)

    elif request.method == 'DELETE':
        like = ProductLike.objects.filter(user=user, product=product).first()
        if like:
            like.delete()
            product.update_likes_count()
            return Response(LikeResponseSerializer(
                {"detail": "Like removed."}
            ).data, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(LikeResponseSerializer(
                {"detail": "You haven't liked this product yet."}
            ).data, status=status.HTTP_400_BAD_REQUEST)
