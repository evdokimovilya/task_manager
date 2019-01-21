from django.urls import path
from task_manager.api.v1 import views

urlpatterns = [
    path('tasks/<int:pk>/', views.TaskView.as_view()),
    path('task/', views.NewTaskView.as_view()),
]
