"""
URL configuration for config project.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    path("account/", include("accounts.urls")),
    path("inventory/", include("inventory.urls")),
]
