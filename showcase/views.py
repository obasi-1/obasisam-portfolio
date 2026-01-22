from django.shortcuts import render, redirect
from django.contrib import messages  # Allows us to show "Success!" alerts
from .models import Project, Profile
from .forms import ContactForm  # Import the new form

def home(request):
    projects = Project.objects.all()
    profile = Profile.objects.first()
    
    # === FORM LOGIC STARTS HERE ===
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Saves to the database!
            messages.success(request, 'Message sent successfully! I will get back to you soon.')
            return redirect('home')  # Reload the page to clear the form
    else:
        form = ContactForm()  # Create an empty form for GET requests
    # ==============================

    return render(request, 'showcase/home.html', {
        'projects': projects, 
        'profile': profile,
        'form': form  # Pass the form to the template
    })