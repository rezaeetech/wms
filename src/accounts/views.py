from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseForbidden
from django.utils.http import url_has_allowed_host_and_scheme


from accounts.models import User
from accounts.forms import UserRegistrationForm, LoginForm


class RegisterView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(
            request,
            template_name="accounts/register.html",
            context={"title": "Register", "form": form},
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
                user = form.save()
                login(self.request, user)
                return redirect("home")

        return render(
            request,
            template_name="accounts/register.html",
            context={"form": form},
        )


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        next_url = request.GET.get("next")
        return render(
            request,
            template_name="accounts/login.html",
            context={
                "title": "Login",
                "form": form,
                "next_url": next_url,
            },
        )

    def post(self, request, *args, **kwargs):
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

                # Get the 'next' parameter from the query string
                next_url = request.POST.get("next_url", "/")

                if not url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
                    next_url = "/"  # Fallback to a safe default

                return redirect(next_url)
            else:
                form.add_error(None, "Invalid username or password")
                return render(
                    request,
                    template_name="accounts/login.html",
                    context={"title": "Login", "form": form},
                )

        return render(
            request,
            template_name="accounts/login.html",
            context={"title": "Login", "form": form},
        )


class ForgetPasswordView(View):
    def get(self, request):
        return render(
            request,
            template_name="accounts/forget-password.html",
            context={"title": "Forget Password"},
        )

    def post(self, request):
        pass


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/")


class RoleRequiredMixin:
    allowed_roles = []

    def dispatch(self, request, *args, **kwargs):
        if request.user.role not in self.allowed_roles:
            return HttpResponseForbidden(
                "You do not have permission to access this page."
            )
        return super().dispatch(request, *args, **kwargs)
