from django.contrib import admin

from inventory.models import (
    Product,
    Inventory,
    Category,
    Supplier,
    Warehouse,
)


admin.site.register(Product)
admin.site.register(Inventory)
admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(Warehouse)
