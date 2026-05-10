from django.contrib import admin

# Register your models here.
# store/admin.py

# ---------------------------------------
from .models import Product, Artisan, ArtisanApplication

admin.site.register(Product)
admin.site.register(Artisan)
admin.site.register(ArtisanApplication)
# ---------------------------------------
