from django.shortcuts import redirect, render
from core.models import CustomUser
from django.contrib import messages
import re
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model


def user_inteface(request):
    return render(request,"core/index.html")


CustomUser = get_user_model()

def user_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        print(email)

        # Authenticate user using email and password
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('user_interface')  # Adjust to your desired redirect URL
            else:
                messages.error(request, 'This account is inactive.')
        else:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'registration/login.html')

def user_register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        email = request.POST.get('email')

        # Check if the password contains at least 10 characters
        if len(password) < 10:
            messages.error(request, 'Password must be at least 10 characters long.')
            return render(request, 'registration/register.html')

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'registration/register.html')

        # Check if email format is valid
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messages.error(request, 'Invalid email format.')
            return render(request, 'registration/register.html')

        # Check if the email is already in use
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email is already in use.')
            return render(request, 'registration/register.html')


        # Create a new user
        user = CustomUser.objects.create_user(name=name, password=password, email=email)
        user.save()

        messages.success(request, 'Registration successful.')
        return redirect('user_login')  # Adjust to your login URL

<<<<<<< HEAD
    return render(request, 'registration/register.html')

def recommendation(request):
    return render(request, 'core/recommandation.html')
=======
    return render(request, 'registration/register.html')
>>>>>>> origin/main
