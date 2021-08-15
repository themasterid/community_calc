# calc/urls.py
from django.urls import path

from .views import BbCreateView, calculator

app_name = 'calc'

urlpatterns = [
    path('calc/', calculator, name='calc'),
    path('calc/add/', BbCreateView.as_view(), name='add'),
]
