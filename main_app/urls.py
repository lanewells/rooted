from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('profile/', views.ProfileDetail.as_view(), name='profile'),
    path('profile/update/', views.ProfileUpdate.as_view(), name='profile-update'),
    path('profile/delete/', views.ProfileDelete.as_view(), name='profile-delete'),
    path('memories/', views.MemoryList.as_view(), name='memory-list'),
    path('memories/create/', views.MemoryCreate.as_view(), name='memory-create'),
    path('memories/<int:pk>/', views.MemoryDetail.as_view(), name='memory-detail'),
    path('memories/<int:pk>/update/', views.MemoryUpdate.as_view(), name='memory-update'),
    path('memories/<int:pk>/delete', views.MemoryDelete.as_view(), name='memory-delete'),
    path('memories/my-memories/', views.my_memories, name='my-memories'),
    path('comments/<int:pk>/update/', views.CommentUpdate.as_view(), name='comment-update'), 
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/update/', views.update_account, name='account-update'),
]