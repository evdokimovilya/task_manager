# task_manager

- create local_settings.py in task_mananger/ with variables "SECRET_KEY", "ALLOWED_HOSTS", "DATABASES"
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py loaddata task_manager/fixtures/task_status.json
- celery -A task_manager worker -l info --concurrency=1
