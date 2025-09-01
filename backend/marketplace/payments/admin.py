from django.contrib import admin
from .models import Payment

class PaymentsAdmin(admin.ModelAdmin):
    list_display = ("amount", "stripe_payment_id", "status", "stripe_payment_method_data")

admin.site.register(Payment, PaymentsAdmin)