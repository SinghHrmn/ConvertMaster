from django.contrib import admin
from django.urls import path,include
from accounts import urls as myaccounturls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('convert/',include(myaccounturls),name="blog")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)