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

current_section = "Inventory"
current_section_url = "inventory_list"


class InventoryListView(ListView):
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


class InventoryDetailView(DetailView):
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


class InventoryCreateView(CreateView):
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


class InventoryUpdateView(UpdateView):
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


class InventoryDeleteView(DeleteView):
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
