from ckeditor.fields import RichTextField
from django.db import models, transaction
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    article = models.CharField(
        _("Article"),
        max_length=6,
        unique=True,
        editable=False)
    name = models.CharField(_("Name"), max_length=255)
    about = models.TextField(_("About"), null=True, blank=True)

    AVAILABILITY_CHOICES = [
        (_('In stock'), _('In stock')),
        (_('Check availability'), _('Check availability')),
    ]
    availability = models.CharField(
        _("Availability"),
        max_length=20,
        choices=AVAILABILITY_CHOICES,
        default=_('Check availability')
    )
    likes = models.PositiveIntegerField(_("Likes"), default=0)
    reviews_count = models.PositiveIntegerField(_("Reviews count"), default=0)
    warranty = models.CharField(
        _("Warranty"),
        max_length=50,
        default='Нет'
    )
    price = models.IntegerField(_("Price"))
    description = RichTextField(_("Description"))
    category = models.CharField(_("Category"), max_length=255)
    free_delivery = models.BooleanField(_("Free delivery"), default=False)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    def __str__(self):
        return self.name

    def delivery_message(self):
        return _("Free delivery within a day") if self.free_delivery else ""

    def save(self, *args, **kwargs):
        if not self.article:
            with (transaction.atomic()):
                last_product = Product.objects.all().order_by('article').last()
                if last_product:
                    last_article = int(last_product.article)
                    self.article = str(last_article + 1).zfill(5)
                else:
                    self.article = '10000'

                while Product.objects.filter(article=self.article).exists():
                    self.article = str(int(self.article) + 1).zfill(5)
        super(Product, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

class Review(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='Reviews',
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
