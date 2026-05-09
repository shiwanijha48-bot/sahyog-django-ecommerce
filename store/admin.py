from django.contrib import admin

# Register your models here.
# store/admin.py

# ---------------------------------------
from .models import Product,Artisan

admin.site.register(Product)
admin.site.register(Artisan)
# ---------------------------------------
