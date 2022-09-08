from django.shortcuts import render, redirect

# Create your views here.


def login(request):
    return render(request, 'authorization/login.html')


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        print('Username Submitted: {} ' .format(email, password))
        return redirect('register')
    return render(request, 'authorization/register.html')
