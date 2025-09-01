from django.db import models
from django.conf import settings


class Profile(models.Model):
    """Abstract base for shared profile fields (seller + customer)."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="%(class)s_profile",  # becomes seller_profile / customer_profile
    )
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]

    def __str__(self):
        # Prefer full name if available, else username
        if hasattr(self.user, "get_full_name"):
            full_name = self.user.get_full_name()
            if full_name:
                return full_name
        return self.user.get_username()

    def display_name(self):
        """Readable name for admin list display."""
        return str(self)
    display_name.short_description = "Name"


class SellerProfile(Profile):
    company_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="seller_logos/", null=True, blank=True)
    banner = models.ImageField(upload_to="seller_banners/", null=True, blank=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.company_name} ({super().__str__()})"


class CustomerProfile(Profile):
    shipping_address = models.JSONField(default=dict, blank=True)
    preferences = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return f"Customer: {super().__str__()}"
