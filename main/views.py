from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
from main.forms import ProductForm, CategoryForm
from main.models import Product, Category

def wish(request):
    products = Product.objects.all()
    return render(request, 'main/wish.html', {'products': products})


def category_list(request):
    total_count = Category.objects.count()
    requested_count = request.GET.get('count')

    try:
        count = int(requested_count)
        if count < 1:
            count = 1
        elif count > total_count:
            count = total_count
    except (TypeError, ValueError):
        count = total_count

    categories = Category.objects.all()[:count]

    return render(request, 'main/index.html', {
        'categories': categories,
        'category_count': total_count,
        'current_count': count
    })


def product_list(request):
    total_count = Product.objects.count()
    requested_count = request.GET.get('count')

    try:
        count = int(requested_count)
        if count < 1:
            count = 1
        elif count > total_count:
            count = total_count
    except (TypeError, ValueError):
        count = total_count

    products = Product.objects.all()[:count]

    return render(request, "main/wish.html", {
        'products': products,
        'total_count': total_count,
        'current_count': count
    })


def create_product(request):
    error = ''
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("wish")
        else:
            error = "Перевірте дані"

    form = ProductForm()
    way_name = "Додавання товару"
    return render(request, 'main/create_product.html', {
        'form': form,
        'error': error,
        'way_name': way_name
    })


def create_category(request):
    error = ''
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            error = "Перевірте дані"

    form = CategoryForm()
    way_name = "Додавання категорії"
    return render(request, 'main/create_category.html', {
        'form': form,
        'error': error,
        'way_name': way_name
    })


class ProductsView(DetailView):
    model = Product
    template_name = 'main/product_view.html'
    context_object_name = "product"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class CategoryView(DetailView):
    model = Category
    template_name = 'main/category_view.html'
    context_object_name = "category"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class ProductsUpdate(UpdateView):
    model = Product
    template_name = 'main/create_product.html'
    form_class = ProductForm
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class CategoryUpdate(UpdateView):
    model = Category
    template_name = 'main/create_category.html'
    form_class = CategoryForm
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class ProductsDelete(DeleteView):
    model = Product
    template_name = "main/delete_product.html"
    success_url = "/wish/"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class CategoryDelete(DeleteView):
    model = Category
    template_name = "main/delete_category.html"
    success_url = "/"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
