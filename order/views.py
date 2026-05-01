from django.shortcuts import render, redirect
from .forms import OrderForm


def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = OrderForm()

    return render(request, 'order/form.html', {'form': form})


def success(request):
    return render(request, 'order/success.html')

def index(request):
    return render(request, 'order/index.html')
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import OrderForm


def login_view(request):
    error_message = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')

        error_message = 'Invalid username or password.'

    return render(request, 'order/login.html', {
        'error_message': error_message
    })


@login_required(login_url='login')
def index(request):
    return render(request, 'order/index.html')


@login_required(login_url='login')
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = OrderForm()

    return render(request, 'order/form.html', {'form': form})


@login_required(login_url='login')
def success(request):
    return render(request, 'order/success.html')


@login_required(login_url='login')
def edit_profile(request):
    return render(request, 'order/edit_profile.html')


def logout_view(request):
    logout(request)
    return redirect('login')
