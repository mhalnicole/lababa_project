from django.shortcuts import render, redirect
from .models import Transaction
from .forms import TransactionForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

def index(request):
    if not request.user.is_authenticated:
        return redirect('/transaction/login/')

    transactions = Transaction.objects.all()
    return render(request, 'transaction/index.html', {'transactions': transactions})

def add_transaction(request):
    if not request.user.is_authenticated:
        return redirect('/transaction/login/')

    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/transaction/')
    else:
        form = TransactionForm()

    return render(request, 'transaction/addNewTransaction.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/transaction/')
        else:
            return render(request, 'transaction/login.html', {'error': 'Invalid credentials'})

    return render(request, 'transaction/login.html')


def logout_view(request):
    logout(request)
    return redirect('/transaction/login/')


def edit_profile(request):
    return render(request, 'transaction/edit_profile.html')