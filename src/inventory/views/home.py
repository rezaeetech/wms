from django.shortcuts import render

from orders.models import Order


def home_view(request):
    orders = Order.objects.all()

    context = {
        "current_section_url": "home",
        "orders": orders,
    }
    return render(request, "home.html", context=context)
