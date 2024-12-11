from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('profile/', views.profile, name='profile'),
    # path('relatives/', views.relatives, name='relatives'),
    path('memories/', views.MemoryList.as_view(), name='memory-list'),
    path('memories/<int:pk>/', views.MemoryDetail.as_view(), name='memory-detail'),
    path('memories/create/', views.MemoryCreate.as_view(), name='memory-create'),
    path('memories/my-memories/', views.my_memories, name='my-memories'),
    
]