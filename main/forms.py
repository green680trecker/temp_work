from .models import Product, Category

from django.forms import ModelForm, TextInput, Select

class ProductForm(ModelForm):
    class Meta:
        model = Product

        fields = ['title', 'price', 'product_qty', 'category']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назва Товару'
            }),
            'price': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ціна Товару'
            }),
            'product_qty': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Кількість Товару'
            }),
            'category': Select(attrs={
                'class': 'form-control'
            })


        }


class CategoryForm(ModelForm):
    class Meta:
        model = Category

        fields = ['title']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назва Товару'
            })

        }