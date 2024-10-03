from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    supplier = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    sku = models.CharField(max_length=20, unique=True)
    path_images = models.CharField(max_length=255)

    def __str__(self):
        return self.name