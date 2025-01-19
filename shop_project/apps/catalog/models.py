from ckeditor.fields import RichTextField
from django.db import models, transaction
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(_("Category Name"), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class SubCategory(models.Model):
    name = models.CharField(_("Subcategory Name"), max_length=255)
    category = models.ForeignKey(
        Category,
        related_name="subcategories",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Subcategory")
        verbose_name_plural = _("Subcategories")


class SubSubCategory(models.Model):
    name = models.CharField(_("Subsubcategory Name"), max_length=255)
    subcategory = models.ForeignKey(
        SubCategory,
        related_name="subsubcategories",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Subsubcategory")
        verbose_name_plural = _("Subsubcategories")


class Product(models.Model):
    article = models.CharField(
        _("Article"),
        max_length=6,
        unique=True,
        editable=False
    )
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

    # Добавляем связь с категориями, подкатегориями и подподкатегориями
    category = models.ForeignKey(
        Category,
        related_name="products",
        on_delete=models.CASCADE,
        help_text=_("Category to which this subcategory belongs.")
    )
    subcategory = models.ForeignKey(
        SubCategory,
        related_name="products",
        on_delete=models.CASCADE,
        null = True,
        blank = True
    )
    subsubcategory = models.ForeignKey(
        SubSubCategory,
        related_name="products",
        on_delete=models.CASCADE,
        null = True,
        blank = True
    )

    free_delivery = models.BooleanField(_("Free delivery"), default=False)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    def __str__(self):
        return self.name

    def delivery_message(self):
        if self.free_delivery:
            return _("Free delivery within a day")
        return None

    def save(self, *args, **kwargs):
        if not self.article:
            last_product = Product.objects.all().order_by('article').last()
            if last_product:
                last_article = int(last_product.article)
                self.article = str(last_article + 1).zfill(5)
            else:
                self.article = '10000'

            while Product.objects.filter(article=self.article).exists():
                self.article = str(int(self.article) + 1).zfill(5)
        super(Product, self).save(*args, **kwargs)

    def update_likes_count(self):
        self.likes = self.likes_set.count()
        self.save()

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")


class ProductLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='likes_set',
                                on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'product']

    def __str__(self):
        return f"{self.user} likes {self.product}"
