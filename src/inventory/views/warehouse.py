from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from inventory.models import Warehouse
from inventory.forms import WarehouseForm

current_section = "Warehouse"
current_section_url = "warehouse_list"


class WarehouseListView(ListView):
    model = Warehouse
    template_name = "inventory/warehouse_list.html"
    context_object_name = "warehouses"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Warehouse List"
        context["current_section"] = current_section
        context["current_section_url"] = current_section_url
        context["current_action"] = "List"
        return context


class WarehouseDetailView(DetailView):
    model = Warehouse
    template_name = "inventory/warehouse_detail.html"
    context_object_name = "warehouse"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Warehouse Detail"
        context["current_section"] = current_section
        context["current_section_url"] = current_section_url
        context["current_action"] = "Detail"
        return context


class WarehouseCreateView(CreateView):
    model = Warehouse
    template_name = "inventory/warehouse_form.html"
    form_class = WarehouseForm
    success_url = reverse_lazy("warehouse_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Warehouse"
        context["current_section"] = current_section
        context["current_section_url"] = current_section_url
        context["current_action"] = "Create"
        return context


class WarehouseUpdateView(UpdateView):
    model = Warehouse
    template_name = "inventory/warehouse_form.html"
    form_class = WarehouseForm
    success_url = reverse_lazy("warehouse_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Warehouse"
        context["current_section"] = current_section
        context["current_section_url"] = current_section_url
        context["current_action"] = "Edit"
        return context


class WarehouseDeleteView(DeleteView):
    model = Warehouse
    template_name = "inventory/warehouse_delete.html"
    success_url = reverse_lazy("warehouse_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Warehouse"
        context["current_section"] = current_section
        context["current_section_url"] = current_section_url
        context["current_action"] = "Delete"
        return context
