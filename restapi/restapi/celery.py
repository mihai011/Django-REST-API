import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restapi.settings')

app = Celery('restapi')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()