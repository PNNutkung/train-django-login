from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import re
# Create your views here.
def index(req):
    return render(req, 'login/index.html')

def login(req):
    username = req.POST['username']
    password = req.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(req, user)
        return render(req, 'login/main_page.html')
    else:
        return render(req, 'login/index.html', {
            'error_message': 'Your username or password is wrong.'
        })

def logout(req):
    logout(req)
    return render(req, 'login/index.html')

def register(req):
    return render(req, 'login/register.html')

def create_new_user(req):
    username = req.POST['username']
    password = req.POST['password']
    confirm_password = req.POST['confirm_password']
    email = req.POST['email']
    firstname = req.POST['firstname']
    lastname = req.POST['lastname']
    if User.objects.get(username=username) is not None:
        return render(req, 'login/register.html', {
            'error_message': 'This username has already taken.'
        })
    elif password != confirm_password:
        return render(req, 'login/register.html', {
            'error_message': 'Your password is not match.'
        })
    elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
        return render(req, 'login/register.html', {
            'error_message': 'Your email is not valid.'
        })
    else:
        user = User.objects.create_user(username, email=email, password=password)
        return render(req, 'login/index.html', {
            'error_message': 'Register successfully.'
        })

def not_found(req):
    raise Http404('Page not found!')
