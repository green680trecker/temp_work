from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from main.models import Product


# Create your views here.

def index(request):
    return render(request, "main/index.html")

def wish(request):
    products = Product.objects.all()
    return render(request, 'main/wish.html', {'products': products})