from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Home Page</h1>')

def my_memories(request):
    return render(request, 'memories/my_memories.html')