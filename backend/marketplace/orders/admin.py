from django.contrib import admin
from .models import Order

class OrdersAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'total_amount', 'status')

admin.site.register(Order, OrdersAdmin)

