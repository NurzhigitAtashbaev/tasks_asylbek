from django.db import models


class Shop(models.Model):
    title = models.CharField(max_length=255)


class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    price = models.IntegerField(null=False)
    count = models.IntegerField(null=False)