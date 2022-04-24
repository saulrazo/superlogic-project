from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('true', views.true, name='true'),
    path('sets', views.sets, name='sets'),
]