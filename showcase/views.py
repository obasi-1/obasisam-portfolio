from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from .models import Project, Profile
from .forms import ContactForm

def home(request):
    projects = Project.objects.prefetch_related('tags').all()
    profile = Profile.objects.first()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # 1. Save to Database
            form.save()
            
            # 2. Prepare the Email
            subject = f"Portfolio Message from {form.cleaned_data['name']}"
            message = f"Sender: {form.cleaned_data['email']}\n\nMessage:\n{form.cleaned_data['message']}"
            
            # 3. Send the Email (Try/Except prevents crashes if email fails)
            try:
                send_mail(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER, # From (You)
                    [settings.EMAIL_HOST_USER], # To (You)
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Email Error: {e}") # Prints error to console, but keeps site running

            messages.success(request, 'Message sent! I will be in touch.')
            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'showcase/home.html', {
        'projects': projects, 
        'profile': profile,
        'form': form
    })