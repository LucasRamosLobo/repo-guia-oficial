from django.contrib import admin
from .models import Categoria, Local, Cidade, Plano


admin.site.register(Local)
admin.site.register(Categoria)
admin.site.register(Cidade)
admin.site.register(Plano)
