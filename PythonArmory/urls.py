from django.contrib import admin
from django.conf.urls import include, url
from PythonArmory.views import pyArmory

urlpatterns = [
    url(r'^$', pyArmory, name='Python Armory'),

]