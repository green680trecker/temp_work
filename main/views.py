from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from main.models import Product, Category



def index(request):
    categories = Category.objects.all()
    return render(request, "main/index.html", {"categories": categories})

def wish(request):
    products = Product.objects.all()
    return render(request, 'main/wish.html', {'products': products})