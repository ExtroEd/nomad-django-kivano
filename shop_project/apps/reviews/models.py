from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.catalog.models import Product

class Review(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='reviews',
        on_delete=models.CASCADE
    )
    name = models.CharField(_("Name"), max_length=255)
    comment = models.TextField(_("Comment"))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.name} on {self.product.name}"

    class Meta:
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")
