from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price", "stock_quantity", "category")

admin.site.register(Product, ProductAdmin)