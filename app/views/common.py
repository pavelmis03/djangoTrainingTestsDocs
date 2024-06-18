from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest


# Create your views here.
def index_page(request: WSGIRequest):
    pagename = "pages/index.html"
    context = {}
    return render(request, pagename, context)
