from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('my-memories/', views.my_memories, name='my-memories'),
]