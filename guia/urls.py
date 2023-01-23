from .views import home, sobre
from django.urls import path

urlpatterns = [
    path("", home, name="home"),
    path("sobre/", sobre, name="sobre"),

    
]