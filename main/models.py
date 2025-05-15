from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=220)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default='', null=False, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/{self.id}"

    class Meta():
        ordering = ('title',)
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

class Product(models.Model):
    title = models.CharField(max_length=220)
    price = models.FloatField()
    product_qty = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(default='', null=False, unique=True)

    def get_absolute_url(self):
        return f"/wish/{self.id}"

    def __str__(self):
        return self.title

    class Meta():
        ordering = ('title',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукти'