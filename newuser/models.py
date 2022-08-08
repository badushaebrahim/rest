from django.db import models

# Create your models here.

class Items(models.Model):
    title = models.TextField()
    discription = models.TextField()
    status = models.BooleanField(default=False)