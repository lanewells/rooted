from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import RelativeProfile, Memory, Comment
from .forms import MemoryForm, UserForm

## HOME
def home(request):
    return HttpResponse('<h1>Home Page</h1>')

## USER & PROFILE
class ProfileDetail(LoginRequiredMixin, DetailView):
    model = RelativeProfile
    template_name = 'main_app/profile/profile_detail.html'

    def get_object(self):
        return self.request.user.relativeprofile
    
for user in User.objects.all():
    if not hasattr(user, 'relativeprofile'):
        RelativeProfile.objects.create(user=user)

def signup(request):
    error_message = ''
    form = UserForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Signup successful!')
            login(request, user)
            return redirect('memories-list')
        else:
            error_message = 'Invalid sign up - try again'
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

## MEMORIES
@login_required
def my_memories(request):
    return render(request, 'main_app/memories/my_memories.html')

class MemoryList(LoginRequiredMixin, ListView):
    model = Memory
    template_name = 'main_app/memories/memory_list.html'
    # paginate_by = 9

class MemoryDetail(LoginRequiredMixin, DetailView):
    model = Memory
    template_name = 'main_app/memories/memory_detail.html'

class MemoryCreate(LoginRequiredMixin, CreateView):
    model = Memory
    form_class = MemoryForm
    template_name = 'main_app/memories/memory_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('memory-detail', kwargs={'pk': self.object.pk})

class MemoryUpdate(LoginRequiredMixin, UpdateView):
    model = Memory
    fields = ['title', 'description', 'memory_date']
    # Does this need something special because the form I wanna reuse is specified in forms.py?

class MemoryDelete(LoginRequiredMixin, DeleteView):
    model = Memory
    success_url = '/memories/'

## COMMENTS
class CommentList(LoginRequiredMixin, ListView):
    model = Comment
    template_name = 'main_app/comments/comment_list.html'

# class CommentCreate(LoginRequiredMixin, CreateView):
#     model = Comment
#     fields = ['text']
#     template_name = 'main_app/comments/comment_form.html'

# class CommentUpdate(LoginRequiredMixin, UpdateView):
#     model = Comment
#     fields = ['text']