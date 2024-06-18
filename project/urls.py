from django.contrib import admin
from django.urls import path

from app.views.common import index_page, check_page, profile_page
from app.views.auth import registration_page, login_page, logout_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page),
    path('login/', login_page),
    path('logout/', logout_page),
    path('reg/', registration_page),
    path('check/', check_page),
    path('profile/', profile_page),
]
