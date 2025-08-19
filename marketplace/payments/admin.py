from django.contrib import admin
from .models import Payments

class PaymentsAdmin(admin.ModelAdmin):
    list_display = ("amount", "stripe_payment_id", "status", "stripe_payment_method_data")

admin.site.register(Payments, PaymentsAdmin)