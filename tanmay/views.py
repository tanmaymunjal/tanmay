from django.shortcuts import render
from django.contrib import admin

def index(request):
    return render(request, 'initial.html') #returns the initial.html

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

