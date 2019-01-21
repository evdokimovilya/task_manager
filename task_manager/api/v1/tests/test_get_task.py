from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from task_manager.common.tests.test import TestFactory
from task_manager.models import Task, TaskStatus
from django.utils import timezone
from datetime import time


class CreateTaskTest(TestFactory, TestCase):

    def setUp(self):
        super(CreateTaskTest, self).setUp()
        default_status = TaskStatus.objects.get(slug='completed')
        start_time = timezone.now()
        execution_time = time(hour=0, minute=0, second=10)
        self.task = Task.objects.create(status=default_status, start_time=start_time, execution_time=execution_time)
        self.invalid_task_pk = 3

    def test_get_task_valid(self):
        c = APIClient()
        response = c.get(f'/api/v1/tasks/{self.task.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_task_invalid(self):
        c = APIClient()
        response = c.get(f'/api/v1/tasks/{self.invalid_task_pk}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
