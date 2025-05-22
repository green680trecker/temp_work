from tastypie.resources import ModelResource
from main.models import Category, Product

class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        allowed_methods = ['get']

class ProductResource(ModelResource):
    class Meta:
        queryset = Product.objects.all()
        resource_name = 'products'
        allowed_methods = ['get']
