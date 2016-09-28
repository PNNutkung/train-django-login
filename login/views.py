from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.urls import reverse

# Create your views here.
def index(req):
    return render(req, 'login/index.html')

def login(req):
    username = req.POST['username']
    password = req.POST['password']
    return render(req, 'login/main_page.html')

def logout(req):
    return render(req, 'login/index.html')

def register(req):
    return render(req, 'login/register.html')

def create_new_user(req):
    return None

def not_found(req):
    raise Http404('Page not found!')
