from django.contrib import admin

from orders.models import (
    Order,
    OrderItems,
    Customer,
)


admin.site.register(Order)
admin.site.register(OrderItems)
admin.site.register(Customer)
