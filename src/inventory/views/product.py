from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from inventory.models import Product
from inventory.forms import ProductForm

current_section = "Product"
current_section_url = "product_list"


class ProductListView(ListView):
    model = Product
    template_name = "inventory/product_list.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Product List"
        context["current_section"] = current_section
        context["current_section_url"] = current_section_url
        context["current_action"] = "Product List"
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "inventory/product_detail.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Product Detail"
        context["current_section"] = current_section
        context["current_section_url"] = current_section_url
        context["current_action"] = "Detail"
        return context


class ProductCreateView(CreateView):
    model = Product
    template_name = "inventory/product_form.html"
    form_class = ProductForm

    success_url = reverse_lazy("product_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Product"
        context["current_section"] = current_section
        context["current_section_url"] = current_section_url
        context["current_action"] = "Create"
        return context


class ProductUpdateView(UpdateView):
    model = Product
    template_name = "inventory/product_form.html"
    form_class = ProductForm

    success_url = reverse_lazy("product_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Product"
        context["current_section"] = current_section
        context["current_section_url"] = current_section_url
        context["current_action"] = "Edit"
        return context


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "inventory/product_delete.html"
    success_url = reverse_lazy("product_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Product"
        context["current_section"] = current_section
        context["current_section_url"] = current_section_url
        context["current_action"] = "Delete"
        return context