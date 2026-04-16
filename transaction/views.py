from django.shortcuts import render, redirect
from .models import Transaction
from .forms import TransactionForm

def index(request):
    transactions = Transaction.objects.all()
    return render(request, 'transaction/index.html', {'transactions': transactions})

def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/transaction/')
    else:
        form = TransactionForm()

    return render(request, 'transaction/addNewTransaction.html', {'form': form})