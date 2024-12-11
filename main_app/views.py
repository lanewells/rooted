from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import Relative, Memory, Comment

def home(request):
    return HttpResponse('<h1>Home Page</h1>')

def profile(request, relative_id):
    relative = Relative.objects.get(id=relative_id)
    return render(request, 'main_app/profile.html', {'relative':relative})

def relatives(request):
    return render(request, 'main_app/relatives.html')

# def memory_detail(request, memory_id):
#     memory = Memory.objects.get(id=memory_id)
#     return render(request, 'memories/memory_detail.html', {'memory': memory})

def my_memories(request):
    return render(request, 'main_app/memories/my_memories.html')

class MemoryList(ListView):
    model = Memory
    template_name = 'main_app/memories/memory_list.html'
    # paginate_by = 9

class MemoryDetail(DetailView):
    model = Memory
    template_name = 'main_app/memories/memory_detail.html'

