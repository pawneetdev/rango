from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Welcome</h1><br><a href = '/rango/about'>About</a>")

def about(request):
    return HttpResponse("<h1>Welcome to about us page.</h1>")
