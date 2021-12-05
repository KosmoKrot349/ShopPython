from django.db import models

class Order(models.Model):
    userEmail = models.CharField(max_length=225)
    productId = models.IntegerField()
    quantity = models.IntegerField()
    date = models.DateField()
    status = models.BooleanField()

class Product(models.Model):
    Name = models.CharField(max_length=225)
    Desc = models.CharField(max_length=9999, default='')
    StorageQuantity = models.IntegerField()
    PricePerUnit = models.IntegerField()
    img = models.ImageField()
