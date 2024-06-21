from django.shortcuts import render, redirect
from django.views import View
from .models import CustomUser
from .forms import CustomUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout


class HomeView(View):
    def get(self, request):
        # Your view logic here
        return render(request, 'home.html')


class RegisterView(View):
    def get(self, request):
        create_form = CustomUserForm()
        context = {
            'form':create_form
        }
        return render(request, 'register.html', context=context)

    def post(self, request):
        create_form = CustomUserForm(data=request.POST, files=request.FILES)
        if create_form.is_valid():
            create_form.save()
            return redirect('users:login')
        else:
            context = {
                'form': create_form
            }
            return render(request, 'login.html', context=context)


class LoginView(View):
    def get(self, request):
        login_form = AuthenticationForm()
        return render(request, 'login.html', context={'form': login_form})

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('home')
        return render(request, 'login.html', context={'form': login_form})


class LogoutView(LoginView):
    def get(self, request):
        logout(request)
        return redirect('home')




