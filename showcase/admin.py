from django.contrib import admin
from .models import Project, Tag, Profile, ContactMessage

admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(Profile)
admin.site.register(ContactMessage)