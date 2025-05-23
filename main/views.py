from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index_view(request):
    return render(request, 'main/index.html')


def registry_view(request):
    return render(request, 'main/registry.html')

def profile_view(request):
    return render(request, 'main/profile.html')