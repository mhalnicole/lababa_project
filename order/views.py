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
from django.shortcuts import render

# Create your views here.
