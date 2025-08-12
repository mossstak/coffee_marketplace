from django.db import models

# Create your models here.
class Product():
      
    
    
    productId = models.IntegerField(primary_key=True)
    productName = models.CharField(max_length=255)
    
    