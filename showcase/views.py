from django.shortcuts import render
from .models import Project, Profile  # Import Profile

def home(request):
    projects = Project.objects.all()
    # Get the first profile object, or None if it doesn't exist
    profile = Profile.objects.first()
    
    return render(request, 'showcase/home.html', {
        'projects': projects, 
        'profile': profile
    })