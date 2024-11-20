from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from inventory.models import Category
from inventory.forms import CategoryForm

current_section = "Category"
current_section_url = "category_list"


class CategoryListView(ListView):
    model = Category
    template_name = "inventory/category_list.html"
    context_object_name = "categories"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Category List"
        context["current_section"] = current_section
        context["current_section_url"] = current_section_url
        context["current_action"] = "List"
        return context


class CategoryDetailView(DetailView):
    model = Category
    template_name = "inventory/category_detail.html"
    context_object_name = "category"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Category Detail"
        context["current_section"] = current_section
        context["current_section_url"] = current_section_url
        context["current_action"] = "Detail"
        return context


class CategoryCreateView(CreateView):
    model = Category
    template_name = "inventory/category_form.html"
    form_class = CategoryForm
    success_url = reverse_lazy("category_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create Category"
        context["current_section"] = current_section
        context["current_section_url"] = current_section_url
        context["current_action"] = "Create"
        return context


class CategoryUpdateView(UpdateView):
    model = Category
    template_name = "inventory/category_form.html"
    form_class = CategoryForm
    success_url = reverse_lazy("category_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Category"
        context["current_section"] = current_section
        context["current_section_url"] = current_section_url
        context["current_action"] = "Edit"
        return context


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "inventory/category_delete.html"
    success_url = reverse_lazy("category_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Category"
        context["current_section"] = current_section
        context["current_section_url"] = current_section_url
        context["current_action"] = "Delete"
        return context