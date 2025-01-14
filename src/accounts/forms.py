from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from accounts.models import User


class UserRegistrationForm(UserCreationForm):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": _("Full Name"),
            }
        ),
    )
    username = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": _("Username"),
            }
        ),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": _("Email"),
            }
        ),
    )
    phone_number = forms.CharField(
        max_length=15,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": _("Phone Number"),
            }
        ),
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": _("Password"),
            }
        ),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": _("Confirm Password"),
            }
        ),
    )

    class Meta:
        model = User
        fields = [
            "name",
            "username",
            "email",
            "phone_number",
            "password1",
            "password2",
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.name = self.cleaned_data.get("name")
        user.username = self.cleaned_data.get("username")
        user.email = self.cleaned_data.get("email")
        user.phone_number = self.cleaned_data.get("phone_number")

        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": _("Username"),
            }
        ),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": _("Password"),
            }
        ),
    )
    remember = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "id": "remember",
            }
        ),
    )
