from .models import Task, TaskStatus
from django.contrib import admin


@admin.register(TaskStatus)
class TaskStatusAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['pk', 'celery_id', 'start_time', 'status']
