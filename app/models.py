
from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)    

class FavoriteProducts(models.Model):
    
    client = models.ForeignKey(
        to=Client, 
        on_delete=models.CASCADE,
        related_name='favorite_products',
    )
    product = models.CharField(max_length=255)

    class Meta:
        unique_together = [
            ('client', 'product')
        ]

    