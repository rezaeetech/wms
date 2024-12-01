from django.db import models
from django.utils.translation import gettext_lazy as _


class Inventory(models.Model):
    product = models.ForeignKey(
        to="inventory.product",
        verbose_name=_("Product"),
        on_delete=models.CASCADE,
    )
    warehouse = models.ForeignKey(
        to="inventory.warehouse",
        verbose_name=_("Warehouse"),
        on_delete=models.SET_NULL,
        null=True,
    )

    quantity = models.IntegerField(
        verbose_name=_("Quantity"),
        default=0,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        unique_together = ("product", "warehouse")
        verbose_name = _("Inventory")
        verbose_name_plural = _("Inventories")

    def __str__(self):
        return (f"{self.product.name} - {self.warehouse.name}"
                "(Qty: {self.quantity})")

    def save(self, *args, **kwargs):
        if self.quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        super().save(*args, **kwargs)

    def adjust_stock(self, delta):
        """
        Adjust stock by a delta value (positive or negative).
        """
        self.quantity += delta
        if self.quantity < 0:
            raise ValueError("Stock cannot be negative after adjustment.")
        self.save()
