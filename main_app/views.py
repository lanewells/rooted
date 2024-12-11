from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import RelativeProfile, Memory, Comment
from .forms import MemoryForm


def home(request):
    return HttpResponse('<h1>Home Page</h1>')

# def profile(request, relative_id):
#     relative = RelativeProfile.objects.get(id=relative_id)
#     return render(request, 'main_app/profile.html', {'relative':relative})

# def relatives(request):
#     return render(request, 'main_app/relatives.html')

def my_memories(request):
    return render(request, 'main_app/memories/my_memories.html')

class MemoryList(ListView):
    model = Memory
    template_name = 'main_app/memories/memory_list.html'
    # paginate_by = 9

class MemoryDetail(DetailView):
    model = Memory
    template_name = 'main_app/memories/memory_detail.html'

class MemoryCreate(CreateView):
    model = Memory
    form_class = MemoryForm
    template_name = 'main_app/memories/memory_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('memory-detail', kwargs={'pk': self.object.pk})

class CommentList(ListView):
    model = Comment
    template_name = 'main_app/comments/comment_list.html'

class CommentCreate(CreateView):
    model = Comment
    fields = ['text', 'description', 'memory_date']
    template_name = 'main_app/comment/comment_form.html'