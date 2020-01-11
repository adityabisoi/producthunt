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
    return render(request,'accounts/login.html')

def logout(request):
    return render(request,'accounts/signup.html')