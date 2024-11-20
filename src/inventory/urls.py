"""
URL configuration for Inventory app.
"""

from django.urls import path

from inventory import views


urlpatterns = [
    # Products URLs
    path(
        "products/",
        views.ProductListView.as_view(),
        name="product_list",
    ),
    path(
        "products/<int:pk>/",
        views.ProductDetailView.as_view(),
        name="product_detail",
    ),
    path(
        "products/create/",
        views.ProductCreateView.as_view(),
        name="product_create",
    ),
    path(
        "products/<int:pk>/update/",
        views.ProductUpdateView.as_view(),
        name="product_update",
    ),
    path(
        "products/<int:pk>/delete/",
        views.ProductDeleteView.as_view(),
        name="product_delete",
    ),

    # Inventory URLs
    path(
        "",
        views.InventoryListView.as_view(),
        name="inventory_list",
    ),
    path(
        "<int:pk>/",
        views.InventoryDetailView.as_view(),
        name="inventory_detail",
    ),
    path(
        "create/",
        views.InventoryCreateView.as_view(),
        name="inventory_create",
    ),
    path(
        "<int:pk>/update/",
        views.InventoryUpdateView.as_view(),
        name="inventory_update",
    ),
    path(
        "<int:pk>/delete/",
        views.InventoryDeleteView.as_view(),
        name="inventory_delete",
    ),

    # Supplier URLs
    path(
        "suppliers/",
        views.SupplierListView.as_view(),
        name="supplier_list",
    ),
    path(
        "suppliers/<int:pk>/",
        views.SupplierDetailView.as_view(),
        name="supplier_detail",
    ),
    path(
        "suppliers/create/",
        views.SupplierCreateView.as_view(),
        name="supplier_create",
    ),
    path(
        "suppliers/<int:pk>/update/",
        views.SupplierUpdateView.as_view(),
        name="supplier_update",
    ),
    path(
        "suppliers/<int:pk>/delete/",
        views.SupplierDeleteView.as_view(),
        name="supplier_delete",
    ),

    # Category URLs
    path(
        "categories/",
        views.CategoryListView.as_view(),
        name="category_list",
    ),
    path(
        "categories/<int:pk>/",
        views.CategoryDetailView.as_view(),
        name="category_detail",
    ),
    path(
        "categories/create/",
        views.CategoryCreateView.as_view(),
        name="category_create",
    ),
    path(
        "categories/<int:pk>/update/",
        views.CategoryUpdateView.as_view(),
        name="category_update",
    ),
    path(
        "categories/<int:pk>/delete/",
        views.CategoryDeleteView.as_view(),
        name="category_delete",
    ),

    # Warehouse URLs
    path(
        "warehouses/",
        views.WarehouseListView.as_view(),
        name="warehouse_list",
    ),
    path(
        "warehouses/<int:pk>/",
        views.WarehouseDetailView.as_view(),
        name="warehouse_detail",
    ),
    path(
        "warehouses/create/",
        views.WarehouseCreateView.as_view(),
        name="warehouse_create",
    ),
    path(
        "warehouses/<int:pk>/update/",
        views.WarehouseUpdateView.as_view(),
        name="warehouse_update",
    ),
    path(
        "warehouses/<int:pk>/delete/",
        views.WarehouseDeleteView.as_view(),
        name="warehouse_delete",
    ),
]
