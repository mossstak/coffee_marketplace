from django.db import models
from django.conf import settings

# Create your models here.

# Shared fields live in an abstract base (NO User field here)


class Profile(models.Model):
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ("-created_at")

class SellerProfile(Profile):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="seller_profile"
    )
    company_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='seller_logos/', null=True, blank=True)
    banner = models.ImageField(
        upload_to='seller_banners/', blank=True, null=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        u = getattr(self.user, "get_username", lambda: str(self.user))()
        return f"{self.company_name}({u})"


class CustomerProfile(Profile):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="customer_profile"
    )
    # JSONFields kept flexible for now
    shipping_address = models.JSONField(default=dict, blank=True)
    preferences = models.JSONField(default=dict, blank=True)

    def __str__(self):
        u = getattr(self.user, "get_username", lambda: str(self.user))()
        return f"Customer {u}"