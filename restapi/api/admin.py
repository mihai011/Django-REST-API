from django.contrib import admin
from rest_framework.authtoken.models import Token
from api.models import PowerRequest, FactorialRequest, FibonaciRequest

# Register your models here.

admin.register(Token)
admin.register(PowerRequest)
admin.register(FactorialRequest)
admin.register(FibonaciRequest)