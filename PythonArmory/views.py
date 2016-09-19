from django.shortcuts import render
from django.template.response import TemplateResponse
from PythonArmory.models import armorySearch
# Create your views here.

def pyArmory(request):
    myString = "This is a python string"
    data = armorySearch.objects.all()
    return TemplateResponse(request, 'PythonArmory/index.html',{"data": data, "myString": myString})