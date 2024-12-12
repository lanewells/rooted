from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('profile/', views.ProfileDetail.as_view(), name='profile'),
    path('profile/edit/', views.ProfileUpdate.as_view(), name='profile-update'),
    path('profile/delete/', views.ProfileDelete.as_view(), name='profile-delete'),
    path('memories/', views.MemoryList.as_view(), name='memory-list'),
    path('memories/<int:pk>/', views.MemoryDetail.as_view(), name='memory-detail'),
    path('memories/create/', views.MemoryCreate.as_view(), name='memory-create'),
    path('memories/my-memories/', views.my_memories, name='my-memories'),


    
]