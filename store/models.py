from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# ------ ARTISAN SECTION---------
class Artisan(models.Model):
    user = models.OneToOneField(
    User,
    on_delete=models.CASCADE,
    null=True,
    blank=True,
    related_name='artisan'
)
    name = models.CharField(max_length=100)
    village = models.CharField(max_length=100)
    craft = models.CharField(max_length=100)
    story = models.TextField()
    image = models.ImageField(upload_to='artisans/')

    def __str__(self):
        return self.name
    
class ArtisanApplication(models.Model):
    user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    null=True
)
    name = models.CharField(max_length=200)
    village = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    craft = models.CharField(max_length=200)
    story = models.TextField()
    image = models.ImageField(upload_to='applications/')
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    approved = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

#  ----------- PRODUCT ------------
class Product(models.Model):
    artisan = models.ForeignKey(Artisan, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    def __str__(self):
        return self.name
    
# ---------- ORDER BOOKING - CART -------------
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    payment_method = models.CharField(
        max_length=50,
        default='Cash on Delivery'
    )
    total_amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.full_name