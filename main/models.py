from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=220)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)  # сначала сохраняем, чтобы получить ID
        if is_new and not self.slug:
            self.slug = str(self.id)
            Category.objects.filter(pk=self.pk).update(slug=self.slug)

    def get_absolute_url(self):
        return f"/{self.slug}"

    class Meta:
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
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new and not self.slug:
            self.slug = str(self.id)
            Product.objects.filter(pk=self.pk).update(slug=self.slug)

    def get_absolute_url(self):
        return f"/wish/{self.slug}"

    class Meta:
        ordering = ('title',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукти'
