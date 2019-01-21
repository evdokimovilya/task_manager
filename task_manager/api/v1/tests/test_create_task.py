from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from task_manager.common.tests.test import TestFactory


class CreateTaskTest(TestFactory, TestCase):

    def test_create_task(self):
        c = APIClient()
        response = c.get('/api/v1/task/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
