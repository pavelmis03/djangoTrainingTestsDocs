from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.decorators import login_required

from app.statistic.texttool import TextStatistic

def index_page(request: WSGIRequest):
    pagename = "pages/index.html"
    context = {
        "flag": "{flag:DoYouWantToTestThis?}"
    }
    return render(request, pagename, context)


@login_required
def check_page(request: WSGIRequest):
    pagename = "pages/check.html"
    context = {}
    if not(text := request.GET.get("text")):
        return render(request, pagename, context)
    statistic = TextStatistic(text)
    context["statistic"] = statistic
    return render(request, pagename, context)