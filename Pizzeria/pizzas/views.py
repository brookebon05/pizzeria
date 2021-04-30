from django.shortcuts import render
from .models import Pizza, Toppings, Comment  # Post
from datetime import datetime, date

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


def comments(request, pizza_id):
    if request.method == "GET" and request.GET.get("btn1"):
        comment = request.GET.get("comment")
        Comment.objects.create(
            pizza_id=pizza_id,
            text=comment,
            date_added=date.today(),
        )
    comments = Comment.objects.filter(pizza=pizza_id)
    # post = Post.objects.get(id=pizza_id)
    context = {"pizza": pizza, "comments": comments}
    return render(request, "pizzas/comments.html", context)
