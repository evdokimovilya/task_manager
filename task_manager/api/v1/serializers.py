from rest_framework import serializers
from task_manager.models import Task
from django.conf import settings


class TaskViewSerializer(serializers.ModelSerializer):
    status = serializers.SlugRelatedField(read_only=True, slug_field='title')
    create_time = serializers.DateTimeField(read_only=True, format=settings.DATE_FORMAT)
    start_time = serializers.DateTimeField(read_only=True, format=settings.DATE_FORMAT)
    time_to_execute = serializers.TimeField(source='execution_time')

    class Meta:
        model = Task
        fields = ('status', 'create_time', 'start_time', 'time_to_execute')
