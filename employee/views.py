from django.shortcuts import render
from . import models
# Create your views here.

def index(request):
    context = {}
    employees = models.Employee.objects.all()
    context['employees'] = employees
    return render(request, 'index.html', context)

def filter(request, id):
    context = {}
    employees = models.Employee.objects.filter(department=id)
    context['employees'] = employees
    return render(request, 'index.html', context)


def about(request):
    
    return render(request, 'about.html')