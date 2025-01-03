from uuid import uuid4

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """
    Custom manager for the User model,
        providing user and superuser creation methods.
    """

    def create_user(self, email, username, password=None, **extra_fields):
        """
        Create and return a regular user with a username, email, and password.
        """

        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        """
        Create and return a superuser with a username, email, and password.
        """

        extra_fields.setdefault("role", "admin")
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model for authentication
        using email and username as unique identifiers.
    """

    ADMIN = "admin"
    MANAGER = "manager"
    STAFF = "staff"

    ROLE_CHOICES = [
        (ADMIN, _("Admin")),
        (MANAGER, _("Manager")),
        (STAFF, _("Staff")),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
    )
    name = models.CharField(
        verbose_name=_("Full Name"),
        max_length=100,
    )
    username = models.CharField(
        verbose_name=_("Username"),
        max_length=50,
        unique=True,
    )
    password = models.CharField(
        verbose_name=_("Password"),
        max_length=128,
    )
    phone_number = models.CharField(
        verbose_name=_("Phone Number"),
        max_length=15,
        blank=True,
        null=True,
    )
    email = models.EmailField(
        verbose_name=_("Email"),
        unique=True,
    )
    role = models.CharField(
        verbose_name=_("Role"),
        choices=ROLE_CHOICES,
        max_length=10,
        default=STAFF,
    )
    is_active = models.BooleanField(
        verbose_name=_("Active Status"),
        default=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )
    is_superuser = models.BooleanField(
        default=False,
    )

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        """
        Return the string representation of the user, which is the username.
        """
        return self.username
