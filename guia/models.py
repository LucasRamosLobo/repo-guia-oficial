from django.db import models
from autoslug import AutoSlugField
from django.shortcuts import reverse
from django.conf import settings

class Cidade(models.Model):
    Nome = models.CharField(max_length=200, null=True)

    slug = AutoSlugField(populate_from="Nome")
    def __str__(self):
        return self.Nome

class Categoria(models.Model):
    Nome = models.CharField(max_length=200, null=True)

    slug = AutoSlugField(populate_from="Nome")
    def __str__(self):
        return self.Nome

class Plano(models.Model):
    Nome = models.CharField(max_length=200, null=True)

    slug = AutoSlugField(populate_from="Nome")
    def __str__(self):
        return self.Nome

class Local(models.Model):
    Plano = models.ForeignKey(Plano, on_delete=models.CASCADE)
    Nome = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from="Nome")
    FotoPincipal = models.CharField(max_length=400)
    Foto1=models.CharField(max_length=400, default='non-exist')
    Foto2=models.CharField(max_length=400, default='non-exist')
    Foto3=models.CharField(max_length=400, default='non-exist')
    Foto4=models.CharField(max_length=400, default='non-exist')
    Foto5=models.CharField(max_length=400, default='non-exist')
    Foto6=models.CharField(max_length=400, default='non-exist')
    Foto7=models.CharField(max_length=400, default='non-exist')
    Foto8=models.CharField(max_length=400, default='non-exist')
    Foto9=models.CharField(max_length=400, default='non-exist')
    Foto10=models.CharField(max_length=400, default='non-exist')
    SobreLocal = models.TextField()
    WhatsApp = models.CharField(max_length=200, default='non-exist')
    Instagram = models.CharField(max_length=200, default='non-exist')
    FaceBook = models.CharField(max_length=200, default='non-exist')
    Site = models.CharField(max_length=200, default='non-exist')
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    Cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    Endereço = models.CharField(max_length=200)

    def __str__(self):
        return self.Nome


    def get_url(self):
        return reverse("detail", kwargs={
            "slug":self.slug,
            "slug2": self.Cidade
          
        })
