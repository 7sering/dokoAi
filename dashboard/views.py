from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

#* Login
def login(request):
    if request.method == 'POST':
        email = request.POST['email'].replace(' ', '').lower()
        password = request.POST['password']

        user = auth.authenticate(username=email, password=password)
        if user:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials please check again')
            return redirect('login')

    return render(request, 'dashboard/login.html')

#* Register
def register(request):
    if request.method == 'POST':
        email = request.POST['email'].replace(' ', '').lower()
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if not password == confirm_password:
            messages.error(request, 'Passwords Do Not Matched')
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'User With This Email Already Existed')
            return redirect('register')

        user = User.objects.create_user(
            email=email, username=email, password=password)
        user.save()

        auth.login(request, user)
        return redirect('dashboard')

    return render(request, 'dashboard/register.html')


def dashboard(request):
    return render(request, 'dashboard/dashboard.html')
