from unicodedata import category
from django.shortcuts import HttpResponse, render
from django.views.generic import TemplateView

from goods.models import Products

class IndexView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Home - Главная"
        context['content'] = "Магазин мебели Home"
        context['text_on_page'] = "Хороший магазин"
        return context


class AboutView(TemplateView):
    template_name = "main/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'home - О нас'
        context['content'] = 'О нас'
        context['text_on_page'] = 'Лучший магазин (по моему мнению)'
        return context



# def index(request) -> HttpResponse:

#     context = {
#         'title': 'home - Главная',
#         'content': 'Магазин мебели - HOME',
#     }

#     return render(request, 'main/index.html', context)

# def about(request) -> HttpResponse:
#     context = {
#         'title': 'home - О нас',
#         'content': 'О нас',
#         'text_on_page': 'Лучший магазин (по моему мнению)'
#     }

#     return render(request, 'main/about.html', context)



