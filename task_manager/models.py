from django.db import models


class TaskStatus(models.Model):
    title = models.CharField(name='title', max_length=255)
    slug = models.SlugField(name='slug', max_length=255)

    def __str__(self):
        return self.title


class Task(models.Model):
    status = models.ForeignKey(TaskStatus, related_name='status_tasks', on_delete=models.SET_NULL, blank=True,
                               null=True)
    create_time = models.DateTimeField(name='create_time', auto_now_add=True)
    start_time = models.DateTimeField(name='start_time', null=True)
    execution_time = models.TimeField(name='execution_time', null=True)
    celery_id = models.CharField(name='celery_id', max_length=255, blank=True)

    def __str__(self):
        return self.celery_id
