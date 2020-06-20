#define my routes
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('create', views.create),
    path('game', views.game),
    path('click', views.click),
    path('reset', views.reset)
]