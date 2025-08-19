from django.db import models
from django.contrib.auth.models import AbstractUser


class CartItem(models.Model):
    quantity = models.IntegerField(default=0)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    add_at = models.DateTimeField(auto_now_add=True)


class Role(models.TextChoices):
    ADMIN = "ADMIN", "Admin"
    SELLER = "SELLER", "Seller"
    CUSTOMER = "CUSTOMER", "Customer"


class User(AbstractUser):
    cart_item = models.ForeignKey(
        CartItem,
        on_delete=models.CASCADE,
        related_name="accounts",
        null=True,       
        blank=True,      
        default=None     
    )
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
