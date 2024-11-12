"""
URL configuration for accounts app.
"""

from django.urls import path

from accounts import views


urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
    path(
        "forget-password/",
        views.ForgetPasswordView.as_view(),
        name="forget-password"
    ),
    path("logout/", views.LogoutView.as_view(), name="logout"),
]
