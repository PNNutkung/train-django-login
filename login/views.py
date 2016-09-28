from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.urls import reverse

# Create your views here.
def index(req):
    return render(req, 'login/index.html')

def login(req):
    return None

def not_found(req):
    raise Http404('Page not found!')
