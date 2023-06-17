from django.urls import path
from .views import Tasklist, TaskCreate, TaskUpdate,TaskDelete, TaskDetailView, CustomLoginView, RegisterView
from django.contrib.auth.views import LogoutView




urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('list/', Tasklist.as_view(), name='task'),
    path('create/', TaskCreate.as_view(), name='task_Create'),
    path('update/<int:pk>/', TaskUpdate.as_view(), name='task_update'),
    path('delete/<int:pk>/', TaskDelete.as_view(), name='task_delete'),
    path('details/<int:pk>/', TaskDetailView.as_view(), name='task_details')
]