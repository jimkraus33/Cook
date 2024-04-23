from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import UserRegisterForm, UserLoginForm

# Create your views here.
def register(request):
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created!')
            return HttpResponseRedirect(reverse_lazy('login'))
    return render(request, 'accounts/register.html', {
        'form': form
    })


def login(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return HttpResponseRedirect(reverse_lazy('index'))
    return render(request, 'accounts/login.html', {
        'form': form
    })


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse_lazy('login'))
