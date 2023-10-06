from django.shortcuts import render

def menu(request):
    return render(request, 'menu.html')

def home(request):
    return render(request, 'home.html')

