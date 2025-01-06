"""
URL configuration for config project.
"""

from django.contrib import admin
from django.urls import path, include

from inventory.views.home import home_view

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", view=home_view, name="home"),

    path("accounts/", include("accounts.urls")),
    path("inventory/", include("inventory.urls")),
    path("orders/", include("orders.urls")),
]
