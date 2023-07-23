from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm, RegistrationForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Authenticate user and log them in
            # (Implementation depends on your authentication system)
            messages.success(request, 'Logged in successfully.')
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'accounts/templates/accounts/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Create a new user account
            form.save()
            messages.success(request, 'Account created successfully.')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/templates/accounts/register.html', {'form': form})
