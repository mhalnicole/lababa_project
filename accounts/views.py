from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')

    error = ""

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            error = "Invalid username or password"

    return render(request, 'accounts/login.html', {'error': error})

def logout_view(request):
    logout(request)
    return redirect('/login/')

@login_required
def edit_profile(request):
    success = False
    error = ""

    if request.method == "POST":
        first_name = request.POST.get("first_name", "").strip()
        last_name = request.POST.get("last_name", "").strip()
        email = request.POST.get("email", "").strip()

        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        success = True

    return render(request, 'accounts/edit_profile.html', {'success': success, 'error': error})