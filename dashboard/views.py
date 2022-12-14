from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

from .models import *
from .forms import *
from .functions import *

# *Decorator for Auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

# Create your views here.


def anonymous_required(function=None, redirect_url=None):
    if not redirect_url:
        redirect_url = 'dashboard'

    actual_decorator = user_passes_test(

        lambda u: u.is_anonymous,
        login_url=redirect_url,
    )

    if function:
        return actual_decorator(function)
    return actual_decorator


# * Login
@anonymous_required
def login(request):
    if request.method == 'POST':
        email = request.POST['email'].replace(' ', '').lower()
        password = request.POST['password']

        user = auth.authenticate(username=email, password=password)
        if user:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials or User Not Existed')
            return redirect('login')

    return render(request, 'dashboard/login.html')

# Register


@anonymous_required
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

# ? Logout Function


@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')


@login_required
def profile(request):
    context = {}

    if request.method == "GET":
        form = ProfileForm(instance=request.user.profile, user=request.user)
        image_form = ProfileImageForm(instance=request.user.profile)
        context["form"] = form
        context["image_form"] = image_form
        return render(request, 'dashboard/profile.html', context)

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user.profile, user=request.user)
        image_form = ProfileImageForm(request.POST, request.FILES, instance=request.user.profile)

        if form.is_valid():
            form.save()
            return redirect('profile')

        if image_form.is_valid():
            image_form.save()
            return redirect('profile')
            
    return render(request, 'dashboard/profile.html')






def blogTopic(request):
    context = {}
    if request.method == 'POST':
        blogIdea = request.POST['blogIdea']
        keywords = request.POST['keywords']

        blogTopics = generateBlogTopicIdea(blogIdea, keywords)
        if len(blogTopics) > 0:
            request.session['blogTopics'] = blogTopics
            return redirect('blog-section')
        else:
            messages.error(request, 'Sorry Unable to generate blog ideas please try again')
            return redirect('blogTopic')

    return render(request, 'dashboard/blogTopic.html', context)


def blogSection(request):
    if 'blogTopics' in request.session:
        pass
    else:
        messages.error(request, 'Start by creating blog topic ideas')
        return redirect('blogTopic')

    context = {}
    context['blogTopics'] = request.session['blogTopics']

    return render(request, 'dashboard/blog-section.html', context)