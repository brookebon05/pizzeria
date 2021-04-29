from django.shortcuts import render
from .models import Pizza, Toppings

# Create your views here.
def index(request):
    # Home Page
    return render(request, "pizzas/index.html")


def pizzas(request):
    pizzas = Pizza.objects.order_by("name")
    context = {"pizzas": pizzas}
    return render(request, "pizzas/pizzas.html", context)
