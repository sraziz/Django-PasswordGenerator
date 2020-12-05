from django.shortcuts import render
from django.http import HttpResponse
import random

def homepage(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def pwd(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+'))
    
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('plen',10))
    
    generatedpassword = ''
    for x in range(length):
        generatedpassword += random.choice(characters)

    return render(request, 'generator/password.html', {'pwd':generatedpassword})
