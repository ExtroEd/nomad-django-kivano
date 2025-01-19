from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.hashers import make_password


class CustomUser(AbstractUser):
    middle_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Отчество")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Телефон")
    address = models.TextField(blank=True, null=True, verbose_name="Адрес доставки")
    newsletter_subscription = models.BooleanField(default=False, verbose_name="Подписка на рассылку")
    email = models.EmailField(unique=True, blank=False)
    password = models.CharField(max_length=128)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',
        blank=True
    )

    def __str__(self):
        return self.username

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
