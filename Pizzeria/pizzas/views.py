from django.shortcuts import render
from .models import Pizza, Toppings

# Create your views here.
def index(request):
    # Home Page
    return render(request, "pizzas/index.html")


def pizzas1(request):
    pizzas = Pizza.objects.order_by("name")
    context = {"pizzas": pizzas}
    return render(request, "pizzas/pizzas1.html", context)


def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = Toppings.objects.order_by("name")

    context = {"pizza": pizza, "toppings": toppings}
    return render(request, "pizzas/pizza.html", context)
