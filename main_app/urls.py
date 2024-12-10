from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('relatives/', views.relatives, name='relatives'),
    path('my-memories/', views.my_memories, name='my-memories'),
    path('family-memories/', views.family_memories, name='family-memories'),
    
]