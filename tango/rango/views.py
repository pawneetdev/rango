from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse("<h1>Welcome</h1><br><a href = '/rango/about'>About</a>")
	context_dict = {'boldmessage': "THIS MESSAGE IS RENDERED BY DJANGO"}
	return render(request, 'rango/index.html', context_dict)

def about(request):
    return HttpResponse("<h1>Welcome to about us page.</h1>")
