 # Лабораторная №8
 
### Розробка функціоналу CRUD.


### Реализація:

1. В програмному застосунку створити файл forms.py та додати код форм для
обраних моделей.

```from .models import Product, Category
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
```

***2-10. Коротко, реалізувати операції CRUD і api для взаємодії для мінімум двох таблиць***

**Головна сторінка категорій**

![img.png](../Report_images/img.png)

**Головна сторінка продуктів**

![img.png](../Report_images/img2.png)

---
**Приклад добавлення категорій**

![img.png](../Report_images/img3.png)

**Приклад добавлення продуктів**

![img.png](../Report_images/img4.png)

---
**Приклад оновлення категорій**

![img.png](../Report_images/img5.png)

**Приклад оновлення продуктів**

![img_1.png](../Report_images/img6.png)

---
**Приклад видалення категорій**

![img.png](../Report_images/img7.png)

**Приклад видалення продуктів**

![img.png](../Report_images/img8.png)

**Результат категорій**

![img.png](../Report_images/img9.png)

**Результат продуктів**

![img.png](../Report_images/img10.png)

---
***11-15***
---

**Категоріі**

![img.png](../Report_images/img11.png)

**Продукти**

![img.png](../Report_images/img12.png)