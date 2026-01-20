from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all().order_by('-date_added')
    return render(request, 'showcase/home.html', {'projects': projects})