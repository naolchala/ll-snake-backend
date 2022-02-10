from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.add_score, name="add_score")
]