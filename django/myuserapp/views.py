from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def mainpage(self):
    return HttpResponse("Hello World")

def homepage(request):
    return render(request,"home.html")

def aboutpage(request):
    return render(request,"about.html")
