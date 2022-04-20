from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('posts.urls')),
    path('group/<slug:slug>/', include('posts.urls')),
    path('', include('calc.urls')),
    path('admin/', admin.site.urls),
]
