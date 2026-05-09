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