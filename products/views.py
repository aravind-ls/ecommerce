from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def index(request):
    products = Product.objects.all()
    return HttpResponse("<h1>Welcome to Django project</h1>")


def about(request):
    return HttpResponse('<h2>About page</h2>')


