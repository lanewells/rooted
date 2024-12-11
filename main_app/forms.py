from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Memory, RelativeProfile

class MemoryForm(forms.ModelForm):
    class Meta:
            model = Memory
            fields = ['title', 'description', 'memory_date']
            # Cite widgets and forms customization
            widgets = {
                  'title': forms.TextInput(attrs={
                        'placeholder': 'Give your memory a title',
                        'class': 'form-control'
                  }),
                  # Cite rows limitation and class form-control
                  'description': forms.Textarea(attrs={
                        'placeholder': 'Tell your story',
                        'rows': 5,
                        'class': 'form-control'
                  }),
                  'memory_date': forms.DateInput(
                      format=('%Y-%m-%d'),
                      attrs={
                            'placeholder': 'Select a date',
                            'type': 'date',
                            'class': 'form-control'
                      }
                )
            }

class UserForm(UserCreationForm):
    birthdate = forms.DateField(
        required=True,
        widget=forms.DateInput(
            format=('%Y-%m-%d'),
            attrs={
                'placeholder': 'Select your birthdate',
                'type': 'date',
                'class': 'form-control',
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'birthdate', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']


class RelativeProfileForm(forms.ModelForm):
    class Meta:
        model = RelativeProfile
        fields = ['birthdate']  
        widgets = {
            'birthdate': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select your birthdate',
                    'type': 'date',
                }
            )
        }