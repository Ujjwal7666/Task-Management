from django.shortcuts import render , redirect
from django.views import View
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout

class LoginView(View):
    def get (self, request):
        return render(request, 'userauth/login.html')
    def post (self, request):
        try:
            if request.method =="POST":
                data = request.POST
                username = data.get("username")
                password = data.get("password")
                user = authenticate (request, username=username, password=password)
                if user:
                    login(request,  user)
                return redirect('home')
            return render(request, 'userauth/login.html', {'error': 'Invalid username or password'})
        except Exception as exe:
            print("sometiing erro", exe)
            return render(request,'userauth/login.html')

    
class LogoutView(View):
    def get (self, request):
        logout(request)
        return redirect('/login')
