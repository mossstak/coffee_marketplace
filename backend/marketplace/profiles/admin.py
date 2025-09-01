from django.contrib import admin
from django.utils.html import format_html
from .models import SellerProfile, CustomerProfile

def avatar_thumb(obj):
    """Render a small avatar preview in admin lists."""
    if obj.avatar and getattr(obj.avatar, "url", None):
        return format_html(
            '<img src="{}" style="height:40px;width:40px;object-fit:cover;border-radius:50%;" />',
            obj.avatar.url,
        )
    return "—"
avatar_thumb.short_description = "Avatar"

@admin.register(SellerProfile)
class SellerProfileAdmin(admin.ModelAdmin):
    list_display = ("company_name", "user", avatar_thumb, "phone_number", "verified", "created_at")
    search_fields = ("company_name", "user__username", "user__email", "phone_number")
    list_filter = ("verified", "created_at")
    # ✅ mark timestamps as read-only
    readonly_fields = (avatar_thumb, "created_at", "updated_at")
    fieldsets = (
        ("Identity", {"fields": ("user", "company_name", "verified")}),
        ("Branding", {"fields": ("logo", "banner", "bio", "phone_number", "avatar", avatar_thumb)}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )

@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ("user", avatar_thumb, "phone_number", "created_at")
    search_fields = ("user__username", "user__email", "phone_number")
    # ✅ mark timestamps as read-only
    readonly_fields = (avatar_thumb, "created_at", "updated_at")
    fieldsets = (
        ("Identity", {"fields": ("user",)}),
        ("Profile", {"fields": ("bio", "phone_number", "avatar", avatar_thumb)}),
        ("Preferences", {"fields": ("shipping_address", "preferences")}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )
