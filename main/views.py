from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello?")

def wish(request):
    return HttpResponse("<h1>I want to play the space station 13</h1>")