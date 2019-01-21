from task_manager.models import TaskStatus
from django.test import TestCase


class TestFactory(TestCase):

    def setUp(self):
        TaskStatus.objects.create(title='In quee', slug='quee')
        TaskStatus.objects.create(title='Run', slug='run')
        TaskStatus.objects.create(title='Completed', slug='completed')
