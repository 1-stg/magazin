from unicodedata import category
from django.shortcuts import HttpResponse, render
from django.core.paginator import Paginator

from goods.models import Categories, Products


def index(request, category_slug=None) -> HttpResponse:

    page = request.GET.get('page', 1 )
    goods = Products.objects.filter(id__lt=10)

    context = {
        'title': 'home - Главная',
        'content': 'Магазин мебели - HOME',
        'goods': goods
    }

    return render(request, 'main/index.html', context)

def about(request) -> HttpResponse:
    context = {
        'title': 'home - О нас',
        'content': 'О нас',
        'text_on_page': 'Лучший магазин (по моему мнению)'
    }

    return render(request, 'main/about.html', context)



