from django.shortcuts import render

# Create your views here.


def index(request):
    # The home page for LEarning Log
    return render(request, "mainapp/index.html")
