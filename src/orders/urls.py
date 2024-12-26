from django.urls import path

from orders import views


urlpatterns = [
    # Orders
    path(
        "",
        views.OrderListView.as_view(),
        name="order_list",
    ),
    path(
        "create/",
        views.OrderCreateView.as_view(),
        name="order_create",
    ),
    path(
        "product-price/<int:product_id>/",
        views.get_product_price,
        name="get_product_price",
    ),

    # Customer
    path(
        "customers/",
        views.CustomerListView.as_view(),
        name="customer_list",
    ),
    path(
        "customers/<int:pk>/",
        views.CustomerDetailView.as_view(),
        name="customer_detail",
    ),
    path(
        "customers/create/",
        views.CustomerCreateView.as_view(),
        name="customer_create",
    ),
    path(
        "customers/<int:pk>/update/",
        views.CustomerUpdateView.as_view(),
        name="customer_update",
    ),
    path(
        "customers/<int:pk>/delete/",
        views.CustomerDeleteView.as_view(),
        name="customer_delete",
    ),

    # Other URLs for inventory
    path(
        "transactions/<int:order_id>/",
        views.InventoryTransactionCreateView.as_view(),
        name="transaction_create",
    ),
]
