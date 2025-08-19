from django.db import models
# from orders.models import Orders

class PaymentStatus(models.TextChoices):
    PENDING = "PENDING", "Pending"
    COMPLETED = "COMPLETED", "Completed"
    FAILED = "FAILED", "Failed"
    REFUNDED = "REFUNDED", "Refunded"

class Payments(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    stripe_payment_id = models.CharField(max_length=255)
    status = models.CharField(
        max_length=255,
        choices=PaymentStatus.choices,
        default=PaymentStatus.PENDING,
    )
    stripe_payment_method_data = models.JSONField(default=dict)
    processed_at = models.DateTimeField(auto_now_add=True)
    failure_reason = models.TextField()        