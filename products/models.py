from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    inventory_quantity = models.IntegerField()
    image = models.CharField(max_length=200)