from django.db import models


class Inventory(models.Model):
    product = models.ForeignKey(
        "inventory.product",
        verbose_name="Product",
        on_delete=models.CASCADE,
    )
    warehouse = models.ForeignKey(
        "inventory.warehouse",
        verbose_name="Warehouse",
        on_delete=models.SET_NULL,
        null=True,
    )

    quantity = models.IntegerField(
        verbose_name="Quantity",
        default=0,
    )

    updated_at = models.DateTimeField(
        verbose_name="Updated at",
        auto_now_add=True,
    )

    def __str__(self):
        return f"Product: {self.product}\n Warehouse: {self.warehouse}"
