from django.contrib import admin
from .models import Project, Tag, Profile  # Added Profile here

admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(Profile)  # Registered Profile here