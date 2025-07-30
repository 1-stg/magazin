from unicodedata import category
from django.shortcuts import HttpResponse, render

from goods.models import Categories


def index(request) -> HttpResponse:

    categories = Categories.objects.all()

    context = {
        'title': 'home - Главная',
        'content': 'Магазин мебели - HOME',
        'categories': categories
    }

    return render(request, 'main/index.html', context)

def about(request) -> HttpResponse:
    context = {
        'title': 'home - О нас',
        'content': 'О нас',
        'text_on_page': 'Лучший магазин (по моему мнению)'
    }

    return render(request, 'main/about.html', context)



