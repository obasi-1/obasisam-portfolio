from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # "upload_to" tells Django which subfolder in 'media' to use
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    github_link = models.URLField(blank=True)
    demo_link = models.URLField(blank=True)
    tags = models.ManyToManyField(Tag, related_name='projects')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title