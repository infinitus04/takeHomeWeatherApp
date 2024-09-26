from django.db import models

# Create your models here.
class UserComment(models.Model):

    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    comment = models.CharField(max_length=200)
