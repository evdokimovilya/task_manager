from task_manager.celery import sleep_task
from task_manager.models import Task, TaskStatus
from task_manager import settings
from celery.signals import task_prerun, task_postrun
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import generics, views
from task_manager.api.v1.serializers import TaskViewSerializer


class NewTaskView(views.APIView):
    # default_status = TaskStatus.objects.get(slug=settings.CELERY_STATUSES.get('PENDING'))

    def get(self, request, *args, **kwargs):
        task = Task()
        task.save()

        # set celery task
        sleep_task.delay(task.pk)

        return Response({"task_number": task.pk})


class TaskView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskViewSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


@task_prerun.connect
def task_prerun_handler(signal, sender, task_id, task, args, kwargs, **extras):
    """Update task before celery starts to execute"""
    task_pk = args[0]
    start_status = TaskStatus.objects.get(slug=settings.CELERY_STATUSES.get('STARTED'))
    task = Task.objects.get(pk=task_pk)
    task.celery_id = task_id
    task.start_time = timezone.now()
    task.status = start_status
    task.save()


@task_postrun.connect
def task_postrun_handler(signal, sender, task_id, task, args, kwargs, **extras):
    """Update task after execution"""
    task_pk = args[0]
    success_status = TaskStatus.objects.get(slug=settings.CELERY_STATUSES.get('SUCCESS'))
    task = Task.objects.get(pk=task_pk)

    # calculate execution time
    execution_time = str(timezone.now() - task.start_time)
    task.execution_time = execution_time
    task.status = success_status
    task.save()
