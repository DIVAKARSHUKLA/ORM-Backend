from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.contrib.auth.models import User
import json
from django.core import serializers

# Create your views here.


def index(request):
    users_list = list(User.objects.filter(is_superuser=False))
    return render(request, 'admin/index.html', {'user': users_list})


def login_view(request):
    if request.method == "POST":
        username = request.POST['user']
        user_pass = request.POST['pass']
        user = authenticate(request, username=username, password=user_pass)
        if user is not None and user.is_superuser:
            #request.session['user'] = user
            login(request, user)
            return redirect('admin')
        else:
            return render(request, 'admin/login.html', {'msg': 'No user found'})
    else:
        return render(request, 'admin/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def userProfile(request, id):
    users_data = list(User.objects.filter(pk=id))
    return render(request, 'admin/users.html', {'user_data': users_data})
