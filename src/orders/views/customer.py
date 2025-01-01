from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from orders.models import Customer
from orders.forms import CustomerForm

from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.views import RoleRequiredMixin

current_section = "customer"
current_section_url = "customer_list"

allowed_roles = [
    "admin",
    "manager",
]  # Create, Update, Delete views only access to admin and manager roles.


class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = "orders/customer_list.html"
    context_object_name = "customers"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Customer List"
        context["current_section"] = current_section
        context["current_section_url"] = current_section_url
        context["current_action"] = "List"
        return context


class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = Customer
    template_name = "orders/customer_detail.html"
    context_object_name = "customer"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Customer Detail"
        context["current_section"] = current_section
        context["current_section_url"] = current_section_url
        context["current_action"] = "Detail"
        return context


class CustomerCreateView(LoginRequiredMixin, RoleRequiredMixin, CreateView):
    model = Customer
    template_name = "orders/customer_form.html"
    form_class = CustomerForm
    success_url = reverse_lazy("customer_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Customer"
        context["current_section"] = current_section
        context["current_section_url"] = current_section_url
        context["current_action"] = "Create"
        return context


class CustomerUpdateView(LoginRequiredMixin, RoleRequiredMixin, UpdateView):
    model = Customer
    template_name = "orders/customer_form.html"
    form_class = CustomerForm
    success_url = reverse_lazy("customer_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit customer"
        context["current_section"] = current_section
        context["current_section_url"] = current_section_url
        context["current_action"] = "Edit"
        return context


class CustomerDeleteView(LoginRequiredMixin, RoleRequiredMixin, DeleteView):
    model = Customer
    template_name = "orders/customer_delete.html"
    success_url = reverse_lazy("customer_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Customer"
        context["current_section"] = current_section
        context["current_section_url"] = current_section_url
        context["current_action"] = "Delete"
        return context
