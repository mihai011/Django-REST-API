from django.contrib.auth.models import User

from celery import shared_task
@shared_task
def create_log(info):
    
    return True