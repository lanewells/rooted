from django.db import models

class Relative(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Memory(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField
    memory_date = models.DateField
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Relative, on_delete=models.CASCADE)

    def __str__(self):
        return f"Memory titled '{self.title}', from {self.memory_date}"

class Comment(models.Model):
    text = models.TextField
    created = models.DateTimeField(auto_now_add=True)
    memory = models.ForeignKey(Memory, on_delete=models.CASCADE)
    created_by = models.ForeignKey(Relative, on_delete=models.CASCADE)
   
    def __str__(self):
        return f"Comment on the memory '{self.memory.title}' by {self.created_by}"
