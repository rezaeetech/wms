from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from accounts.models import User
from accounts.forms import (
    UserRegistrationForm,
    LoginForm
)


class RegisterView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(
            request,
            template_name="accounts/register.html",
            context={
                "title": "Register",
                "form": form
            }
        )

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")

            # Check if the username already exists
            if User.objects.filter(username=username).exists():
                form.add_error("username", "Username is already taken.")

            # Check if the email already exists
            if User.objects.filter(email=email).exists():
                form.add_error("email", "Email is already registered.")

            # If no additional errors, save the user
            if not form.errors:
                form.save()
                return redirect("/")

        return render(
            request,
            template_name="accounts/register.html",
            context={"form": form}
        )


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(
            request,
            template_name="accounts/login.html",
            context={
                "title": "Login",
                "form": form
            }
        )

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            remember = form.cleaned_data.get("remember")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                if not remember:
                    # Set session to expire when the browser is closed
                    request.session.set_expiry(0)
                else:
                    # Set session expiry to 2 weeks (default)
                    request.session.set_expiry(1209600)

                return redirect("/")
            else:
                form.add_error(None, "Invalid username or password")
                return render(
                    request,
                    template_name="accounts/login.html",
                    context={
                        "title": "Login",
                        "form": form
                    }
                )

        return render(
            request,
            template_name="accounts/login.html",
            context={
                "title": "Login",
                "form": form
            }
        )


class ForgetPasswordView(View):
    def get(self, request):
        return render(
            request,
            template_name="accounts/forget-password.html",
            context={"title": "Forget Password"}
        )

    def post(self, request):
        pass


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/")
