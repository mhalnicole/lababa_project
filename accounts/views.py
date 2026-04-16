from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_page(request):
    error = ""

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')  # go to index page
        else:
            error = "Invalid username or password"

    return render(request, 'accounts/login.html', {'error': error})