import json

from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse

from orders.models import OrderItems
from orders.forms import OrderForm, OrderItemFormSet

from inventory.models import Product as ProductModel

current_section = "orders"
current_section_url = "order_create"


class OrderCreateView(View):
    def get(self, request):
        order_form = OrderForm()
        order_item_formset = OrderItemFormSet(
            queryset=OrderItems.objects.none(),
        )

        return render(
            request,
            "orders/order_create.html",
            {
                "order_form": order_form,
                "order_item_formset": order_item_formset,
                "title": "Create Order",
                "current_section": current_section,
                "current_section_url": current_section_url,
                "current_action": "Create",
            },
        )

    def post(self, request):
        order_form = OrderForm(request.POST)
        order_item_formset = OrderItemFormSet()
        product_list = json.loads(request.POST.get("product_list"))

        if order_form.is_valid():
            # Save the order
            order = order_form.save(commit=False)
            order.total_amount = 0  # Initialize total
            order.save()

            # Save the order items
            for item in product_list:
                product = ProductModel.objects.get(id=item["product"])
                order_item = OrderItems.objects.create(
                    order=order,
                    product=product,
                    quantity=int(item["quantity"]),
                    price=product.price,
                )
                order.total_amount += order_item.get_total_price()

            order.save()  # Save the final total amount
            return redirect("orders:order_list")

        return render(
            request,
            "orders/order_create.html",
            {
                "order_form": order_form,
                "order_item_formset": order_item_formset,
                "title": "Create Order",
                "current_section": current_section,
                "current_section_url": current_section_url,
                "current_action": "Create",
            },
        )


def get_product_price(request, product_id):
    try:
        product = ProductModel.objects.get(id=product_id)
        return JsonResponse({"success": True, "price": product.price})
    except ProductModel.DoesNotExist:
        return JsonResponse({"success": False, "error": "Product not found"})
