from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest


def index_page(request: WSGIRequest):
    pagename = "pages/index.html"
    context = {
        "flag": "{flag:DoYouWantToTestThis?}"
    }
    return render(request, pagename, context)
