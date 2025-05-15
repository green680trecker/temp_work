from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('wish/create_product/', views.create_product, name="create_product"),
    path('create_category/', views.create_category, name="create_category"),


    path('', views.category_list, name="index"),
    path("wish/", views.product_list, name="wish"),


    path("wish/<slug:slug>/", views.ProductsView.as_view(), name="wish_view"),
    path("<slug:slug>/", views.CategoryView.as_view(), name="category_view"),


    path("wish/<slug:slug>/update/", views.ProductsUpdate.as_view(), name="wish_update"),
    path("<slug:slug>/update/", views.CategoryUpdate.as_view(), name="category_update"),


    path("wish/<slug:slug>/delete/", views.ProductsDelete.as_view(), name="wish_delete"),
    path("<slug:slug>/delete/", views.CategoryDelete.as_view(), name="category_delete"),
]
