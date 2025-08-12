from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    categorySlug = models.SlugField(max_length=100)
    is_active = models.BooleanField(default=False)

class Product():
    class roast_level(models.TextChoices):
        LIGHT = "LIGHT", "Light"
        MEDIUM_LIGHT = "MEDIUM_LIGHT", "Medium_Light"
        MEDIUM = "MEDIUM", "Medium"
        MEDIUM_DARK = "MEDIUM_DARK", "Medium_Dark"
        DARK = "DARK", "Dark"
    
    class processing_method(models.TextChoices):
        WASHED = "WASHED", "Washed"
        NATURAL = "NATURAL", "Natural"
        HONEY
    
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=2)
    stock_quantity = models.DecimalField(max_digits=2)
    origins = models.CharField(max_length=100)
    
    