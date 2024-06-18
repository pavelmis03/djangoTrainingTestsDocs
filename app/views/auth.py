from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

from app.forms import RegistrationForm, LoginForm

def registration_page(request: WSGIRequest):
    pagename = "pages/reg.html"
    context = {}
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        is_valid = form.is_valid()
        context["form"] = form
        if not is_valid:
            context["errors"] = form.errors
            return render(request, pagename, context)
        name, surname = form.data["first_name"], form.data["second_name"]
        email = form.data["email"]
        username, password = form.data["login"], form.data["password"]
        if len(User.objects.filter(username=username)):
            context["errors"] = {"login": "Пользователь с таким логином уже существует"}
            return render(request, pagename, context)

        user = User.objects.create_user(username, email, password, first_name=name, last_name=surname)
        login(request, user)
        return redirect("/")
    context["form"] = RegistrationForm()
    return render(request, pagename, context)


def login_page(request: WSGIRequest):
    pagename = "pages/login.html"
    context = {}
    if request.method == "POST":
        form = LoginForm(request.POST)
        is_valid = form.is_valid()
        context["form"] = form
        if not is_valid:
            context["errors"] = form.errors
            return render(request, pagename, context)
        username, password = form.data["username"], form.data["password"]
        user = authenticate(username=username, password=password)
        if not user:
            context["errors"] = {"Ошибка данных": "Не удалось войти"}
            return render(request, pagename, context)
        login(request, user)
        return redirect("/")
    context["form"] = LoginForm()
    return render(request, pagename, context)

# @login_required
def logout_page(request: WSGIRequest):
    logout(request)
    return redirect("/")
