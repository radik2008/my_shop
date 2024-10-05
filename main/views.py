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
                        '🔥Только качественные и проверенные товары для готовки на огне🔥'
    }
    return render(request, 'main/about.html', context)


def contacts(request):
    context = {
        'title': 'Contacts - Контакты',
        'content': 'Контакты',
        'text_on_page': 'У нас одни из самых низких цен в России на данную посуду!'
                        'Магазин находиться по адресу г. Магнитогорск, ул. Суворова 16.'
                        'Связаться с нами очень легко👇🏻'
                        '🖊В сообщения группы KAZAN STORE Магнитогорск'
                        'Или по тел.'
                        '☎ 89080433925'
                        '☎ 89068518966'

    }
    return render(request, 'main/about.html', context)

def delivery(request):
    context = {
        'title': 'Delivery - Доставка',
        'content': 'Доставка',
        'text_on_page': '❓ Как заказать товар в нашем магазине?'
                        'Выберите понравившийся товар в наших постах или в каталоге:'
                        'Перейдите по ссылке, чтобы узнать актуальные цены, получить доп.фото или уточнить по деталям'
                        'заказа: vk.me / kazan_store74'
    }
    return render(request, 'main/about.html', context)