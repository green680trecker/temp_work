from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=220)
    created_at = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    title = models.CharField(max_length=220)
    price = models.FloatField()
    product_qty = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
