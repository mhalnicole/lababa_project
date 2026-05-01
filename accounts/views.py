from django.shortcuts import render, redirect
from django.views import View


class LoginView(View):
    template_name = 'accounts/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == "admin" and password == "1234":
            request.session['username'] = username
            return redirect('home')
        else:
            return render(request, self.template_name, {'error': 'Invalid username or password'})

class HomeView(View):
    template_name = 'accounts/home.html'

    def get(self, request):
        if not request.session.get('username'):
            return redirect('login')
        return render(request, self.template_name)

class EditProfileView(View):
    template_name = 'accounts/edit_profile.html'

    def get(self, request):
        if not request.session.get('username'):
            return redirect('login')
        return render(request, self.template_name)

class LogoutView(View):
    def get(self, request):
        request.session.flush()
        return redirect('login')