from django.db import models
from django.conf import settings

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneRel(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    avatar = models.ImageField(upload_to="avatars/", null=True)
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SellerProfile(Profile):
    company_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='seller_logos/')
    banner = models.ImageField(upload_to='seller_banners/')
    tax_id = models.CharField(max_length=30, blank=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.company_name} ({self.user.username})"


class CustomerProfile(Profile):
    shipping_address = models.JSONField(default=dict)
    preferences = models.JSONField(default=dict)

    def __str__(self):
        return f"Customer: {self.user.username}"