from django.contrib import admin
from rest_framework.authtoken.models import Token
from api.models import PowerRequest, FactorialRequest, FibonaciRequest, LogRequest

# Register your models here.

admin.register(Token)
admin.register(LogRequest)
admin.register(PowerRequest)
admin.register(FactorialRequest)
admin.register(FibonaciRequest)