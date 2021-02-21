"""restapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from api.views import power_view, fibonaci_view, factorial_view

from django.conf.urls import url

from django.views.decorators.cache import cache_page

from rest_framework.authtoken import views



urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^api/v1/power/(?P<base>[-]?([0-9]*[.])?[0-9]+)/(?P<exponent>[-]?([0-9]*[.])?[0-9]+)',cache_page(60 * 10)(power_view), name="get_power"),
    path('api/v1/fibonaci/<int:index>',cache_page(60 * 15)(fibonaci_view), name="get_fibonaci"),
    path('api/v1/factorial/<int:index>',cache_page(60 * 15)(factorial_view), name="get_factorial"),
]

# auth api 
urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token)
]