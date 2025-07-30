from importlib.resources import contents
from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Products

def catalog(request) -> HttpResponse:

    goods = Products.objects.all()

    context = {
        'title': 'Home - Каталог',
        'goods': goods
    }
    return render(request, 'goods/catalog.html', context)

def product(request) -> HttpResponse:
    return render(request, 'goods/product.html')
