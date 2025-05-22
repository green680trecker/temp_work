from django.urls import path, include
from tastypie.api import Api
from .resources import CategoryResource, ProductResource


api_category = Api(api_name='v1')
api_category.register(CategoryResource())

api_product = Api(api_name='v1')
api_product.register(ProductResource())

urlpatterns = [
    path('', include(api_category.urls)),
    path('', include(api_product.urls)),
]
