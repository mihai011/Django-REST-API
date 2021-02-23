from django.contrib.auth.models import User

from .models import LogRequest

from celery.decorators import task
import json

@task(queue="logging")
def create_log(info_json):
    
    l = LogRequest(logging_state=json.loads(info_json))
    l.save()

    return True