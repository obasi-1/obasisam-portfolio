from django.contrib import admin
from .models import Project, Tag

# This tells the Admin panel to show these models
admin.site.register(Project)
admin.site.register(Tag)