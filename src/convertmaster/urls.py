from django.contrib import admin
from django.urls import path,include
from accounts import urls as myaccounturls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('convert/',include(myaccounturls),name="blog"),
]