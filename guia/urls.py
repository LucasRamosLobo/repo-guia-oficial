from .views import home, sobre, parceiro
from django.urls import path

urlpatterns = [
    path("", home, name="home"),
    path("guia-sul-da-bahia/", sobre, name="sobre"),
    path("parceiro-guia-sul-da-bahia/", parceiro, name="parceiro"),

]