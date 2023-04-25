from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def SignupView(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST['email']
        password = request.POST['password']
        # password = request.POST.get('password')
        print(firstname, lastname, username, email, password )
        user = User.objects.create_user(username=username, email=email, password=password, first_name=firstname, last_name=lastname)
        user.save()
        messages.success(request, 'Account created successfully! 🙂')
    return render(request, 'signup.html')


def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "🙄 Login credentials incorrect.")
    return render(request, 'login.html')


@login_required(login_url='login')
def HomePageView(request):
    if request.user.is_authenticated:
        # print('Name: ', request.user.get_full_name())
        # print('Last Login: ', request.user.last_login)
        # print('Password: ', request.user.password)
        # print('Email: ', request.user.email)
        data = {
            'name': request.user.get_full_name(),
            'email': request.user.email,
            'last_login': request.user.last_login,
        }
    return render(request, 'home.html', context=data)


def LogoutView(request):
    logout(request)
    return redirect('login')