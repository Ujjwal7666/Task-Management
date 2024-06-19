from django.shortcuts import render , redirect
from django.views import View
from django.contrib.auth.models import User 


class SignupView(View):
    def get(self, request):
        return render(request, 'userauth/signup.html')
    
    def post(self, request):
        try: 
            if request.method == 'POST':
                data = request.POST
                first_name = data.get("firstname")
                last_name = data.get("lastname")
                username = data.get("username")
                email = data.get("email")
                password1 = data.get("password1")
                password2 = data.get("password2")

                if password1 != password2:
                     return render(request, 'userauth/signup.html', {'error_message': 'Passwords do not match.'})
                    
                User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
                return redirect('/login/')
        except Exception as exe:
            print("sometiing erro", exe)
            return render(request,'userauth/signup.html')

        return render(request, 'userauth/signup.html')