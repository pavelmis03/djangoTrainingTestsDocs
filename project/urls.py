from django.contrib import admin
from django.urls import path

from app.views.common import index_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page)
]
