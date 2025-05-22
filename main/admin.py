from django.contrib import admin
from main.models import Category, Product
from . import models

# Register your models here.
# admin.site.register(Category)
# admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('category', 'price',)
    list_editable = ('price',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('title',)
    # list_editable = ('',)