from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from .models import Client


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import Client


class ClientRegistrationForm(forms.ModelForm):
    username = forms.CharField(
        label='Логін',
        widget=forms.TextInput(attrs={
            'placeholder': 'Введіть логін',
            'class': 'form-control custom-input'
        })
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'placeholder': 'Введіть email',
            'class': 'form-control custom-input'
        })
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Введіть пароль',
            'class': 'form-control custom-input'
        })
    )

    class Meta:
        model = Client
        fields = ['username', 'email', 'password', 'name', 'surname', 'phone_number', 'date_birth']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Введіть імʼя',
                'class': 'form-control custom-input'
            }),
            'surname': forms.TextInput(attrs={
                'placeholder': 'Введіть прізвище',
                'class': 'form-control custom-input'
            }),
            'phone_number': forms.TextInput(attrs={
                'placeholder': 'Введіть номер телефону',
                'class': 'form-control custom-input'
            }),
            'date_birth': forms.TextInput(attrs={
                'type': 'date',
                'class': 'form-control custom-input'
            }),
        }

    def save(self, commit=True):

        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password']
        )

        # Потім створюємо Client і повʼязуємо (можна додати ForeignKey до User)
        client = super().save(commit=False)
        client.user = user
        # client.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
            client.save()
        return client

    # password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    #
    # class Meta:
    #     model = Client
    #     fields = ['name', 'surname', 'phone_number', 'date_birth', 'password']
    #     widgets = {
    #         'date_birth': forms.TextInput(attrs={'type': 'date', 'class': 'form-control custom-input'}),
    #         'name': forms.TextInput(attrs={'placeholder': 'Введите имя', 'class': 'form-control custom-input'}),
    #         'surname': forms.TextInput(attrs={'placeholder': 'Введите фамилию', 'class': 'form-control custom-input'}),
    #         'phone_number': forms.TextInput(attrs={'placeholder': 'Введите номер', 'class': 'form-control custom-input'}),
    #         'password': forms.PasswordInput(attrs={'placeholder': 'Введите пароль', 'class': 'form-control custom-input'}),
    #     }
    #
    # def save(self, commit=True):
    #     client = super().save(commit=False)
    #     client.password = make_password(self.cleaned_data['password'])
    #     if commit:
    #         client.save()
    #     return client
