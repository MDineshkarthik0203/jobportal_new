from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User


def register_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')

        # ✅ check if username exists
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {
                'error': 'Username already exists'
            })

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.role = role
        user.save()

        return redirect('/login/')

    return render(request, 'register.html')

def login_page(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    
    # ✅ THIS LINE WAS MISSING
    return render(request, 'login.html')





def logout_page(request):
    logout(request)
    return redirect('/login/')