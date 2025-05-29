from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from main.forms import ClientRegistrationForm


# Create your views here.

def index_view(request):
    return render(request, 'main/index.html')


def registry_view(request):
    if request.method == 'POST':
        form = ClientRegistrationForm(request.POST)
        if form.is_valid():
            client = form.save()
            login(request, client.user)
            return redirect('profile')
    else:
        form = ClientRegistrationForm()
    return render(request, 'main/registry.html', {'form': form})

@login_required
def profile_view(request):
    return render(request, 'main/profile.html', {'user': request.user})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'registration/login.html', {'error': 'Неправильный логин або пароль'})
    return render(request, 'registration/login.html')