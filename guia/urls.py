from .views import home, sobre, parceiro,detail, search
from django.urls import path

urlpatterns = [
    path("", home, name="home"),
    path("guia-sul-da-bahia/", sobre, name="sobre"),
    path("parceiro-guia-sul-da-bahia/", parceiro, name="parceiro"),
    path("<slug2>/<slug>", detail, name="detail"),
    path("search/", search, name="search"),
]