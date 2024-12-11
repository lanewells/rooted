from django import forms
from .models import Memory

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