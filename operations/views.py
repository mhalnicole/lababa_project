from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EmployeeForm

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def addNewEmployee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EmployeeForm()
    return render(request, 'addNewEmployee.html', {'form': form})
