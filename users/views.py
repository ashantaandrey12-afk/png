from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.utils import timezone
from django.urls import reverse
from .models import *

# Create your views here.

def RegisterView(request):
    return render(request, 'register.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user= authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'users/login.html', {'error':'Invalid credentials'})
    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

# Example of role-based access control
@login_required
def admin_dashboard(request):
    if request.user.userprofile.role != 'Admin':
        return redirect('permission_denied')
    return render(request, 'admin/dashboard.html')