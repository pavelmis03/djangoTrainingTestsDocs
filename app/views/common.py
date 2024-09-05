"""
Модуль view, отвечающий за работу с шаблонами основных страниц сайта
"""
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.decorators import login_required
from app.views import TextStatistic

def index_page(request: WSGIRequest):
    """
        Обработчик главной страницы
        :param request: объект запроса
        :return: отрендеренную страницу
    """
    pagename = "pages/index.html"
    context = {
        "flag": "{flag:DoYouWantToTestThis?}"
    }
    return render(request, pagename, context)


@login_required
def check_page(request: WSGIRequest):
    """
        Обработчик страницы статистики статьи
        :param request: объект запроса
        :return: отрендеренную страницу
    """
    pagename = "pages/check.html"
    context = {}
    if not(text := request.GET.get("text")):
        return render(request, pagename, context)
    statistic = TextStatistic(text)
    context["statistic"] = statistic
    return render(request, pagename, context)


@login_required
def profile_page(request: WSGIRequest):
    """
        Обработчик страницы профиля
        :param request: объект запроса
        :return: отрендеренную страницу
    """
    pagename = "pages/profile.html"
    context = {
        "Test": "Smile)",
    }
    return render(request, pagename, context)
