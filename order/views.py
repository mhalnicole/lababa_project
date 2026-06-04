from django.shortcuts import render, redirect, get_object_or_404
from .models import Order
from .forms import OrderForm
from django.contrib.auth.decorators import login_required

@login_required
def order_home(request):
    return render(request, 'order/index.html')

def order_list(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'order/order_list.html', {'orders': orders})

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            return render(request, 'order/success.html', {'order': order})
    else:
        form = OrderForm()
    
    return render(request, 'order/form.html', {'form': form})

def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'order/order_detail.html', {'order': order})


def edit_order(request, id):
    order = get_object_or_404(Order, id=id)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save(commit=False)
            order.order_status = 'Pending'
            order.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)

    return render(request, 'order/edit_order.html', {'form': form, 'order': order})


def delete_order(request, id):
    order = get_object_or_404(Order, id=id)

    if request.method == 'POST':
        order.delete()
        return redirect('order_list')

    return render(request, 'order/delete_order.html', {'order': order})