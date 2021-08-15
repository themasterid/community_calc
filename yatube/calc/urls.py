# calc/urls.py
from django.urls import path

from .views import BbCreateView, calc

app_name = 'calc'

urlpatterns = [
    path('calc/', calc, name='calc'),
]
