from django.shortcuts import render, redirect
from .forms import CustomerForm
from .models import Customer
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib import messages


@login_required
@never_cache
def index(request):
    return render(request, 'customer/index.html')


@login_required
@never_cache
def add_new_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Customer record saved successfully.')
            return redirect('home')

    else:
        form = CustomerForm()

    return render(
        request,
        'customer/addNewCustomer.html',
        {'form': form}
    )


@login_required
@never_cache
def add_new_rating(request):

    ratings = [
        {
            'customer': 'Juan Dela Cruz',
            'score': 5,
            'feedback': 'Excellent service and on-time delivery.'
        },
        {
            'customer': 'Maria Santos',
            'score': 4,
            'feedback': 'Clothes were clean and neatly packed.'
        },
        {
            'customer': 'Pedro Reyes',
            'score': 5,
            'feedback': 'Very satisfied with the laundry service.'
        }
    ]

    return render(
        request,
        'customer/view_customer_ratings.html',
        {'ratings': ratings}
    )


@login_required
@never_cache
def home(request):
    return render(request, 'customer/home.html')


@login_required
@never_cache
def lababa_home(request):
    return render(request, 'customer/lababa_home.html')

@login_required
@never_cache
def manage_customers(request):

    customers = Customer.objects.all()

    return render(
        request,
        'customer/manage_customers.html',
        {'customers': customers}
    )


@login_required
@never_cache
def edit_customer(request, id):

    customer = Customer.objects.get(id=id)

    if request.method == 'POST':

        form = CustomerForm(
            request.POST,
            instance=customer
        )

        if form.is_valid():
            form.save()
            return redirect('manage_customers')

    else:

        form = CustomerForm(instance=customer)

    return render(
        request,
        'customer/edit_customer.html',
        {'form': form}
    )


@login_required
@never_cache
def delete_customer(request, id):

    customer = Customer.objects.get(id=id)

    customer.delete()

    return redirect('manage_customers')