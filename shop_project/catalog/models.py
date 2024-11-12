from itertools import product

from django.db import models


class Product(models.Model):
    article = models.CharField(max_length=6, unique=True, editable=False)
    name = models.CharField(max_length=255)
    about = models.TextField(null=True, blank=True)
    availability = models.CharField(
        max_length=20,
        choices=[('На складе', 'На складе'),
                 ('Уточняйте наличие', 'Уточняйте наличие')],
        default='Уточняйте наличие'
    )
    likes = models.PositiveIntegerField(default=0)
    reviews_count = models.PositiveIntegerField(default=0)
    warranty = models.CharField(max_length=50, default='нет')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=255)
    free_delivery = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def delivery_message(self):
        return "Бесплатная доставка в течении дня" if self.free_delivery \
            else ""

    def save(self, *args, **kwargs):
        if not self.article:
            last_product = Product.objects.all().order_by('article').last()
            if last_product:
                last_article = int(last_product.article)
                self.article = str(last_article + 1).zfill(6)
            else:
                self.article = '10000'
        super(Product, self).save(*args, **kwargs)


class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews',
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.name} on {self.product.name}"
