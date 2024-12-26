from orders.views.order import (  # noqa
    OrderCreateView,
    OrderListView,
    get_product_price,
    InventoryTransactionCreateView,
)

from orders.views.customer import (  # noqa
    CustomerListView,
    CustomerDetailView,
    CustomerCreateView,
    CustomerUpdateView,
    CustomerDeleteView,
)
