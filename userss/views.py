from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        my_user = authenticate(request, username=username, password=password)
        if my_user is not None:
            login(request, my_user)
            return redirect('home')
        else:
            return HttpResponse("☠ Either Username or Password is incorrect. ☠")
    return render(request, 'login.html')


def SignupView(request):
    if request.method == 'POST':
        full_name = request.POST.get('fullname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(full_name, username, email, password )
        my_user = User.objects.create_user(username=username, email=email, password=password)
        my_user.save()
        return HttpResponse("✔✔ User has been created successfully!! ")
    return render(request, 'signup.html')


@login_required(login_url='login')
def HomePageView(request):
    return render(request, 'home.html')


def LogoutView(request):
    logout(request)
    return redirect('login')