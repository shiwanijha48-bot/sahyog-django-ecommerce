from django.db import models

# Create your models here.

# ------ ARTISAN SECTION---------
class Artisan(models.Model):
    name = models.CharField(max_length=100)
    village = models.CharField(max_length=100)
    craft = models.CharField(max_length=100)
    story = models.TextField()
    image = models.ImageField(upload_to='artisans/')

    def __str__(self):
        return self.name
    
class ArtisanApplication(models.Model):
    name = models.CharField(max_length=200)
    village = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    craft = models.CharField(max_length=200)
    story = models.TextField()
    image = models.ImageField(upload_to='applications/')
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    
    artisan = models.ForeignKey(
        Artisan,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.name