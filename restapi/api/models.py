from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


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