from django.db import models
from django.core.validators import MinValueValidator
from django.contrib import admin

# Create your models here.

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        

class PowerRequest(models.Model):

    base = models.FloatField(null=False)
    exponent = models.FloatField(null=False)
    response = models.FloatField(null=True, blank=True,  default=None)
    

class FibonaciRequest(models.Model):

    index = models.PositiveIntegerField(null=False, validators=[MinValueValidator(1)])
    response = models.FloatField(null=True,blank=True, default=None)
    

class FactorialRequest(models.Model):

    index = models.PositiveIntegerField(null=False, validators=[MinValueValidator(1)])
    response = models.FloatField(null=True, blank=True,  default=None)