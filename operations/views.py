from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import EmployeeForm
from .models import Employee

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def addNewEmployee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('viewEmployees')
    else:
        form = EmployeeForm()
    return render(request, 'addNewEmployee.html', {'form': form})

@login_required
def viewEmployees(request):
    employees = Employee.objects.all()
    return render(request, 'viewEmployees.html', {'employees': employees})

@login_required
def editEmployee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('viewEmployees')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'editEmployee.html', {'form': form, 'employee': employee})

@login_required
def deleteEmployee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == 'POST':
        employee.delete()
        return redirect('viewEmployees')
    return render(request, 'deleteEmployee.html', {'employee': employee})
