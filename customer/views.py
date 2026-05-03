from django.shortcuts import render, redirect
from .forms import CustomerForm, RatingForm
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'customer/index.html')


def add_new_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_index')
    else:
        form = CustomerForm()

    return render(request, 'customer/addNewCustomer.html', {'form': form})


def add_new_rating(request):
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_index')
    else:
        form = RatingForm()

    return render(request, 'customer/addNewRating.html', {'form': form})


@login_required
def home(request):
    return render(request, 'customer/home.html')