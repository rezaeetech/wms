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

    def __str__(self):
        return f"Product: {self.product}\n Warehouse: {self.warehouse}"
