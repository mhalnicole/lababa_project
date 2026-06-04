from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def login_page(request):
    error = ""

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', '/order/')
            return redirect(next_url)
        else:
            error = "Invalid username or password"

    return render(request, 'accounts/login.html', {'error': error})

def logout_user(request):
    logout(request)
    return redirect('login')

def edit_profile(request):
    return render(request, 'order/edit_profile.html')