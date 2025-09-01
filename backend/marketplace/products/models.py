from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class RoastLevel(models.TextChoices):
    LIGHT = "LIGHT", "Light"
    MEDIUM_LIGHT = "MEDIUM_LIGHT", "Medium_Light"
    MEDIUM = "MEDIUM", "Medium"
    MEDIUM_DARK = "MEDIUM_DARK", "Medium_Dark"
    DARK = "DARK", "Dark"


class ProcessingMethod(models.TextChoices):
    WASHED = "WASHED", "Washed"
    NATURAL = "NATURAL", "Natural"
    HONEY = "HONEY", "Honey"


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(999)])
    origins = models.CharField(max_length=100)
    roastlevel = models.CharField(
        max_length=100,
        choices=RoastLevel.choices,
        default=RoastLevel.MEDIUM,
    )
    processingmethod = models.CharField(
        max_length=100,
        choices=ProcessingMethod.choices,
        default=ProcessingMethod.NATURAL,
    )
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.ImageField(upload_to="products/")
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
