from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from apps.catalog.models import Product


class Cart(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name="cart",
        verbose_name=_("User")
    )
    session_key = models.CharField(
        max_length=255, null=True, blank=True,
        verbose_name=_("Session Key")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Creation Date")
    )

    def total_items(self):
        return sum(item.quantity for item in self.cart_items.all())

    def total_price(self):
        return sum(item.quantity * item.product.price
                   for item in self.cart_items.all())

    class Meta:
        verbose_name = _("Cart")
        verbose_name_plural = _("Carts")


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,
                             related_name="cart_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1,
                                           verbose_name=_("Quantity"))

    def total_price(self):
        return self.quantity * self.product.price

    class Meta:
        verbose_name = _("Cart Item")
        verbose_name_plural = _("Cart Items")
