from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories


def index(request):
    context = {
        'title': 'Home - Главная',
        'content': 'KAZAN STORE',
        'items': [
            'Чугунные и афганские казаны!',
            'Турецкие самовары',
            'Шампуры и мангалы',
            'Самовары и Тандыры',
            'И многое другое!!!'
        ],

    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'About - О нас',
        'content': 'О нас',
        'text_on_page': 'С нами вкуснее '
                        '🥘Только качественные и проверенные товары для готовки на огне🔥'
    }
    return render(request, 'main/about.html', context)
