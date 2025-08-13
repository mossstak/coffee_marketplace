from django.db import models
from products.models import Product


class OrderStatus(models.TextChoices):
    PENDING = "PENDING", "Pending"
    CONFIRMED = "CONFIRMED", "Confirmed"
    PROCESSING = "PROCESSING", "Processing"
    SHIPPED = "SHIPPED", "Shipped"
    DELIVERED = "DELIVERED", "Delivered"
    CANCELLED = "CANCELLED", "Cancelled"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Orders, on_delete=models.CASCADE, related_name="items")  # type: ignore
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"


class Orders(models.Model):
    order_item = models.ForeignKey(
        OrderItem, on_delete=models.CASCADE, related_name="orders"
    )
    order_number = models.IntegerField(default=0)
    total_amount = models.DecimalField(decimal_places=2)
    shipping_cost = models.DecimalField(decimal_places=2)
    tax_amount = models.DecimalField(decimal_places=2)
    status = models.CharField(
        max_length=100,
        choices=OrderStatus.choices,
        default=OrderStatus.PENDING
    )
    shipping_address = models.TextField()
    billing_address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
