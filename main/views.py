from django.shortcuts import HttpResponse, render

def index(request) -> HttpResponse:
    context = {
        'title': 'home',
        'content': 'Главная страница магазина',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'is_user': False
    }

    return render(request, 'main/index.html', context)

def about(request) -> HttpResponse:
    return HttpResponse('About page')



