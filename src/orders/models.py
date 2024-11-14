from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    class OrderType(models.TextChoices):
        PURCHASE = "Purchase", _("Purchase")
        SALE = "Sale", _("Sale")

    class OrderStatus(models.TextChoices):
        PENDING = "Pending", _("Pending")
        COMPLETED = "Completed", _("Completed")
        CANCELLED = "Cancelled", _("Cancelled")

    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid4,
    )

    customer = models.ForeignKey(
        to="orders.customer",
        verbose_name=_("Customer"),
        on_delete=models.SET_NULL,
        null=True,
        related_name="orders",
    )

    order_type = models.CharField(
        verbose_name=_("Order Type"),
        choices=OrderType.choices,
        max_length=20,
    )
    order_status = models.BooleanField(
        verbose_name=_("Order Status"),
        max_length=20,
        choices=OrderStatus.choices,
        default=OrderStatus.PENDING,
    )
    total_amount = models.DecimalField(
        verbose_name=_("Total amount"),
        max_digits=12,
        decimal_places=2,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f"Order #{self.id.split('-')[0]} - {self.customer.name}"


class OrderItems(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid4,
    )

    order = models.ForeignKey(
        to="orders.order",
        verbose_name=_("Order"),
        on_delete=models.CASCADE,
        related_name="items",
    )
    product = models.ForeignKey(
        to="inventory.product",
        verbose_name=_("Product"),
        on_delete=models.CASCADE,
    )
    quantity = models.PositiveIntegerField(
        verbose_name=_("Quantity"),
    )
    price = models.DecimalField(
        verbose_name=_("Price"),
        max_digits=12,
        decimal_places=2,
    )

    def __str__(self):
        return f"""OrderItem for Order #{self.order.id.split('-')[0]} -
                    {self.product.name}"""

    def get_total_price(self):
        return self.quantity * self.price


class Customer(models.Model):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid4,
    )

    name = models.CharField(
        verbose_name=_("Full Name"),
        max_length=255,
    )
    contact_number = models.CharField(
        verbose_name=_("Contact Number"),
        max_length=20,
    )
    email = models.EmailField(
        verbose_name=_("Email"),
        max_length=255,
    )
    address = models.TextField(
        verbose_name=_("Address"),
    )

    def __str__(self):
        return self.name
