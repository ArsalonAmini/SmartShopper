from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=250)
    asin = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    features = models.CharField(max_length=250)
    images = models.CharField(max_length=250)

    def __str__(self):
        return self.title + ' - ' + self.asin + ' - ' + self.genre + self.features + ' - ' + self.images 
       

