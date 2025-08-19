from django.contrib import admin
from .models import Orders

class OrdersAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'total_amount', 'status')

admin.site.register(Orders, OrdersAdmin)

