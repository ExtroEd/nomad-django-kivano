from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name="orders",
        verbose_name=_("User")
    )

    cart = models.ForeignKey(
        'cart.Cart', on_delete=models.CASCADE, related_name="orders"
    )

    first_name = models.CharField(max_length=100, verbose_name=_("First Name"))
    last_name = models.CharField(max_length=100, verbose_name=_("Last Name"))
    middle_name = models.CharField(max_length=100, null=True, blank=True,
                                   verbose_name=_("Middle Name"))

    phone_number = models.CharField(
        max_length=15,
        verbose_name=_("Phone Number"),
        validators=[RegexValidator(r'^\+?1?\d{9,15}$')],
    )
    international_phone_number = models.CharField(
        max_length=15, null=True, blank=True,
        verbose_name=_("International Phone Number")
    )

    email = models.EmailField(verbose_name=_("Email"))

    delivery_address = models.CharField(max_length=255,
                                        verbose_name=_("Delivery Address"))
    delivery_method = models.CharField(
        max_length=100, choices=[
            ("courier", "Courier in Bishkek (free for orders over 2500 KGS)")]
    )

    payment_method = models.CharField(max_length=100,
                                      choices=[("cash", "Cash")])
    order_comments = models.TextField(null=True, blank=True,
                                      verbose_name=_("Order Comments"))

    status = models.CharField(
        max_length=50,
        choices=[("pending", "Pending"), ("confirmed", "Confirmed"),
                 ("shipped", "Shipped"), ("delivered", "Delivered")],
        default="pending", verbose_name=_("Order Status")
    )

    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_("Order Date"))

    def __str__(self):
        return f"Order {self.id} by {self.first_name} {self.last_name}"

    def send_confirmation_email(self):
        """Отправка email с подтверждением заказа"""
        subject = _("Order Confirmation")
        message = (f"Hello {self.first_name} {self.last_name},\n\nYour order "
                   f"has been confirmed. We'll notify you once it's shipped.")
        send_mail(subject, message, settings.EMAIL_FROM_ADDRESS,
                  [self.email])

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")


@receiver(post_save, sender=Order)
def order_created(sender, instance, created, **kwargs):
    if created:
        instance.send_confirmation_email()
