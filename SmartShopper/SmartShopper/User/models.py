from django.db import models

# Create your models here.

class SignUp(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    Address = models.CharField(max_length=250)

    def __str__(self):
        return self.Address + ' - ' + self.name + ' - ' + self.email 
       
  
class User(models.Model):
    name = models.CharField(max_length=250)
    login = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    signup = models.ForeignKey(SignUp, on_delete=models.CASCADE)