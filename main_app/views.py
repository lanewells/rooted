from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import RelativeProfile, Memory, Comment
from .forms import MemoryForm, UserForm, UserUpdateForm, RelativeProfileForm

## HOME
class Home(LoginView):
    template_name = 'main_app/home.html'

## USER & PROFILE
class ProfileDetail(LoginRequiredMixin, DetailView):
    model = RelativeProfile
    template_name = 'main_app/profile/profile_detail.html'

    def get_object(self):
        return self.request.user.relativeprofile

def signup(request):
    error_message = ''
    form = UserForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            if not hasattr(user, 'relativeprofile'):
                RelativeProfile.objects.create(
                    user=user,
                    birthdate=form.cleaned_data['birthdate']
                )
            messages.success(request, 'Signup successful! Welcome to the family.')
            login(request, user)
            return redirect('memory-list')
        else:
            error_message = 'Invalid sign up - try again'
    context = {'form': form, 'error_message': error_message}
    return render(request, 'main_app/signup.html', context)

class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = RelativeProfile
    fields = ['birthdate']
    template_name = 'main_app/profile/profile_form.html'

    def get_object(self):
        return self.request.user.relativeprofile

    def get_success_url(self):
        return '/profile/'

class ProfileDelete(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'main_app/profile/profile_confirm_delete.html'

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return '/'

@login_required
def update_account(request):
    user_form = UserUpdateForm(instance=request.user)
    profile_form = RelativeProfileForm(instance=request.user.relativeprofile)

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = RelativeProfileForm(request.POST, instance=request.user.relativeprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile') 

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'main_app/account/update_account.html', context)

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