from django.db import models
from django.utils.translation import gettext_lazy as _

from inventory.models import Inventory


class Order(models.Model):
    class OrderType(models.TextChoices):
        PURCHASE = "Purchase", _("Purchase")
        SALE = "Sale", _("Sale")

    class OrderStatus(models.TextChoices):
        PENDING = "Pending", _("Pending")
        COMPLETED = "Completed", _("Completed")
        CANCELLED = "Cancelled", _("Cancelled")

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
    order_status = models.CharField(
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
        return f"Order #{self.id} - {self.customer.name}"


class OrderItems(models.Model):
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
        return f"""OrderItem for Order #{self.order.id} -
                    {self.product.name}"""

    def get_total_price(self):
        return self.quantity * self.price


class Customer(models.Model):
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


class InventoryTransaction(models.Model):
    class TransactionType(models.TextChoices):
        INBOUND = "inbound", _("Inbound")
        OUTBOUND = "outbound", _("Outbound")

    transaction_type = models.CharField(
        max_length=10,
        choices=TransactionType.choices,
        verbose_name=_("Transaction Type"),
    )
    order = models.ForeignKey(
        "orders.Order",
        on_delete=models.CASCADE,
        related_name="inventory_transactions",
        verbose_name=_("Order"),
    )
    warehouse = models.ForeignKey(
        "inventory.Warehouse",
        on_delete=models.CASCADE,
        verbose_name=_("Warehouse"),
    )
    recorded_by = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("Recorded By"),
    )
    transaction_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Transaction Date"),
    )

    class Meta:
        verbose_name = _("Inventory Transaction")
        verbose_name_plural = _("Inventory Transactions")
        ordering = ["-transaction_date"]

    def __str__(self):
        return (
            f"{self.get_transaction_type_display()} - "
            "Order: {self.order.id} - {self.warehouse.name}"
        )

    def save(self, *args, **kwargs):
        """
        Automatically update stock in the associated warehouse
        when the transaction is saved.
        """
        order_items = self.order.items.all()
        for item in order_items:
            product_inventory, created = Inventory.objects.get_or_create(
                product=item.product, warehouse=self.warehouse
            )
            if self.transaction_type == self.TransactionType.INBOUND:
                product_inventory.quantity += item.quantity
            elif self.transaction_type == self.TransactionType.OUTBOUND:
                if product_inventory.quantity < item.quantity:
                    raise ValueError(
                        f"Insufficient stock in {self.warehouse.name} "
                        "for {item.product.name}"
                    )
                product_inventory.quantity -= item.quantity
            product_inventory.save()
        super().save(*args, **kwargs)
