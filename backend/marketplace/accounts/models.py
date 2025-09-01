from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import MinValueValidator


class Role(models.TextChoices):
    ADMIN = "ADMIN", "Admin"
    SELLER = "SELLER", "Seller"
    CUSTOMER = "CUSTOMER", "Customer"

class User(AbstractUser):
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.CUSTOMER
    )
    phone_number = models.CharField(max_length=20, blank=True, unique=True)
    address = models.CharField(max_length=255, blank=True)

    @property
    def is_admin(self):
        return self.role == Role.ADMIN

    @property
    def is_seller(self):
        return self.role == Role.SELLER

    @property
    def is_customer(self):
        return self.role == Role.CUSTOMER


class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name="cart_items")
    quantity = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1)])
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    added_at = models.DateTimeField(auto_now_add=True)
