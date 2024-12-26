import json

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, FormView

from django.http import JsonResponse

from orders.models import OrderItems, Order, InventoryTransaction
from inventory.models import Warehouse as WarehouseModel
from orders.forms import OrderForm, OrderItemFormSet

from inventory.models import Product as ProductModel

current_section = "orders"
current_section_url = "order_list"


class OrderListView(ListView):
    model = Order
    template_name = "orders/orders_list.html"
    context_object_name = "orders"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Orders List"
        context["current_section"] = current_section
        context["current_section_url"] = current_section_url
        context["current_action"] = "List"
        return context


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
            return redirect("order_list")

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


class InventoryTransactionCreateView(FormView):
    def get(self, request, *args, **kwargs):
        order_id = self.kwargs.get("order_id")
        print("//////////////////////////////////////////////////////////////")
        print(order_id)
        order = get_object_or_404(Order, id=order_id)
        order_items = order.items.all()
        warehouses = WarehouseModel.objects.all()

        return render(
            request,
            "orders/transaction_form.html",
            {
                "order_id": order_id,
                "order_items": order_items,
                "warehouses": warehouses,
                "title": "Confirm Transaction",
                "current_section": current_section,
                "current_section_url": current_section_url,
                "current_action": " Transaction",
            },
        )

    def post(self, request, *args, **kwargs):
        order_id = self.kwargs.get("order_id")
        order = get_object_or_404(Order, id=order_id)
        warehouse_id = request.POST.get("warehouse")
        warehouse = get_object_or_404(WarehouseModel, id=warehouse_id)
        order_status = request.POST.get("order_status")
        if order_status in Order.OrderStatus.labels:
            if order.order_type == "Purchase":
                transaction_type = "outbound"
            else:
                transaction_type = "inbound"
            InventoryTransaction.objects.create(
                transaction_type=transaction_type,
                order=order,
                warehouse=warehouse,
                recorded_by=request.user,
            )
            return redirect("orders:order_list")

        raise ValueError(Order)
