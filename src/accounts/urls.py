from django.urls import path
from .views import *

urlpatterns=[

    path('register_user', register_user, name='register'),
    path('', index, name='index'),
    path('login_user', login_user, name='login'),
    path('dashboard', dashboard, name='dashboard'),
    path('logout', logout, name='logout')


]