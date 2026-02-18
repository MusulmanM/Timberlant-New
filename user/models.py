from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    language = models.CharField(max_length=4, default='uz')
    
    
    def __str__(self):
        return self.username
        

class UserFavourite(models.Model):
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} | {self.product}"



class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address_name = models.CharField(max_length=255, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} | {self.address_name}"