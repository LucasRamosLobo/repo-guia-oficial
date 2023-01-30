from django.db import models
from autoslug import AutoSlugField
from django.shortcuts import reverse
from django.conf import settings

class Cidade(models.Model):
    title = models.CharField(max_length=200)

    slug = AutoSlugField(populate_from="title")
    def __str__(self):
        return self.title

class Topic(models.Model):
    title = models.CharField(max_length=200)

    slug = AutoSlugField(populate_from="title")
    def __str__(self):
        return self.title

class Local(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from="title")
    FotoDoAnuncio = models.CharField(max_length=400)
    SobreLocal = models.TextField()
    RedesSociais = models.TextField()
   
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    Cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse("detail", kwargs={
            "slug":self.slug,
        })
