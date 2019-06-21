from django.urls import path
from .views import *

urlpatterns=[

    path("register_user",register_user),
    path("",index),
    path("login_user",login_user),
    path('dashboard',dashboard),
    path('logout',logout)


]