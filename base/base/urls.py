from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path

urlpatterns = [

    path('admin/', admin.site.urls),
     path('', include('iiitnweb.urls')),
     # path('about/', include('iiitnweb.urls')),
]
