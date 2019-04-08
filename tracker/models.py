from django.db import models

# Create your models here.
class Crypto(models.Model):
    name: models.TextField()
    initial: models.CharField(max_length=5)
    desctiption: models.TextField()
    
