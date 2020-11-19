from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from auth_user.forms import UserForm
# Create your views here.

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username') # name attribute of input tag
        password = request.POST.get('password')
        
        user_auth = authenticate(request, username=username, password=password)
        if user_auth:
            login(request, user_auth)
            return redirect('main')
        return redirect('login')
    else:
        if request.user.is_authenticated:
            return redirect('main')
        return render(request, 'auth/login.html')

def register_page(request):
    if request.user.is_authenticated:
        return redirect('main')
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    form = UserForm()
    context = {
        'form': form
    }
    return render(request, 'auth/register.html', context)

def logout_page(request):
    logout(request)
    return redirect('login')
