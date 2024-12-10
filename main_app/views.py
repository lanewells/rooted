from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Home Page</h1>')

def profile(request):
    return render(request, 'main/profile.html')

def relatives(request):
    return render(request, 'main/relatives.html')

def my_memories(request):
    return render(request, 'memories/my_memories.html')

def family_memories(request):
    return render(request, 'memories/family-memories')