from .views import home, sobre, parceiro
from django.urls import path

urlpatterns = [
    path("", home, name="home"),
    path("sobre/", sobre, name="sobre"),
    path("parceiro/", parceiro, name="parceiro"),

]