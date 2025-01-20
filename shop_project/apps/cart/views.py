from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Корзины"])
class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @extend_schema(
        summary="Получить список корзин",
        description="Возвращает список всех доступных корзин. "
                    "Доступно только для чтения, без авторизации."
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Создать корзину",
        description="Создаёт новую корзину, связанную с текущим "
                    "аутентифицированным пользователем."
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary="Получить корзину по ID",
        description="Возвращает данные корзины по указанному ID. "
                    "Требуется указать корректный идентификатор корзины."
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Обновить корзину целиком",
        description="Полностью обновляет корзину по указанному ID. "
                    "Требуется передать все поля корзины в теле запроса."
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        summary="Частично обновить корзину",
        description="Обновляет отдельные поля корзины по указанному ID. "
                    "Указывается только те поля, которые нужно изменить."
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        summary="Удалить корзину",
        description="Удаляет корзину по указанному ID. "
                    "Требуется передать корректный идентификатор корзины."
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@extend_schema(tags=["Предметы в корзинах"])
class CartItemViewSet(ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @extend_schema(
        summary="Получить список предметов в корзинах",
        description="Возвращает список всех предметов, добавленных в корзины."
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Добавить предмет в корзину",
        description="Создаёт новый элемент в указанной корзине. "
                    "Необходимо указать данные предмета и ID корзины."
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary="Получить предмет в корзине по ID",
        description="Возвращает данные предмета по его идентификатору. "
                    "Требуется указать ID предмета."
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Обновить предмет в корзине целиком",
        description="Полностью обновляет данные предмета в корзине. "
                    "Требуется указать все поля."
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        summary="Частично обновить предмет в корзине",
        description="Обновляет отдельные поля предмета в корзине. "
                    "Указываются только те поля, которые нужно изменить."
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        summary="Удалить предмет из корзины",
        description="Удаляет предмет из корзины по указанному ID. "
                    "Требуется передать ID предмета."
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(cart=self.request.data.get('cart'))
