# yatube/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('posts.urls', namespace='main')),
    path('calc/', include('calc.urls', namespace='calc')),
    path('group/<slug:slug>/', include('posts.urls', namespace='post')),
    path('admin/', admin.site.urls),
]
