from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from inventory.models import Inventory
from inventory.forms import InventoryForm

from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.views import RoleRequiredMixin

current_section = "Inventory"
current_section_url = "inventory_list"

allowed_roles = [
    "admin",
    "manager",
]  # Create, Update, Delete views only access to admin and manager roles.


class InventoryListView(LoginRequiredMixin, ListView):
    model = Inventory
    template_name = "inventory/inventory_list.html"
    context_object_name = "inventory_items"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Inventory List"
        context["current_section"] = current_section
        context["current_section_url"] = current_section_url
        context["current_action"] = "List"
        return context


class InventoryDetailView(LoginRequiredMixin, DetailView):
    model = Inventory
    template_name = "inventory/inventory_detail.html"
    context_object_name = "inventory_item"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Inventory Detail"
        context["current_section"] = current_section
        context["current_section_url"] = current_section_url
        context["current_action"] = "Detail"
        return context


class InventoryCreateView(LoginRequiredMixin, RoleRequiredMixin, CreateView):
    model = Inventory
    template_name = "inventory/inventory_form.html"
    form_class = InventoryForm
    success_url = reverse_lazy("inventory_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Inventory"
        context["current_section"] = current_section
        context["current_section_url"] = current_section_url
        context["current_action"] = "Create"
        return context


class InventoryUpdateView(LoginRequiredMixin, RoleRequiredMixin, UpdateView):
    model = Inventory
    template_name = "inventory/inventory_form.html"
    form_class = InventoryForm
    success_url = reverse_lazy("inventory_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Inventory"
        context["current_section"] = current_section
        context["current_section_url"] = current_section_url
        context["current_action"] = "Edit"
        return context


class InventoryDeleteView(LoginRequiredMixin, RoleRequiredMixin, DeleteView):
    model = Inventory
    template_name = "inventory/inventory_delete.html"
    success_url = reverse_lazy("inventory_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Inventory"
        context["current_section"] = current_section
        context["current_section_url"] = current_section_url
        context["current_action"] = "Delete"
        return context
