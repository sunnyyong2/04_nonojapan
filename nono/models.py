from django.db import models

# Create your models here.
class nono(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)