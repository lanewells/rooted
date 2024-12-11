from django.contrib.auth.models import User
from django.db import models

class RelativeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Memory(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    memory_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"Memory titled '{self.title}', from {self.memory_date.strftime('%Y-%m-%d') if self.memory_date else 'No Date'}"

class Comment(models.Model):
    text = models.TextField('Type your comment')
    created = models.DateTimeField(auto_now_add=True)
    memory = models.ForeignKey(Memory, on_delete=models.CASCADE, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f"Comment on the memory '{self.memory.title}' by {self.created_by}"
