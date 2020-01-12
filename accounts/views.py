from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        if request.POST['pass'] == request.POST['repass']:
            try:
                user = User.objects.get(username=request.POST['uname'])
                return render(request,'accounts/signup.html', {'uerror': 'Username already exists'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['uname'], password=request.POST['pass'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request,'accounts/signup.html',{'perror':'Passwords do not match'})
    else:
        return render(request,'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['uname'], password=request.POST['pass'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request,'accounts/login.html',{'error':'Incorrect username or password'})
    else:
        return render(request,'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')