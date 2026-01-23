import requests
from django.core.management.base import BaseCommand
from showcase.models import Project

class Command(BaseCommand):
    help = 'Syncs public repositories from GitHub to the Portfolio database'

    def handle(self, *args, **kwargs):
        username = "obasi-1"
        url = f"https://api.github.com/users/{username}/repos?sort=updated&per_page=6"
        
        self.stdout.write(f"Connecting to GitHub API for {username}...")
        
        response = requests.get(url)
        
        if response.status_code != 200:
            self.stdout.write(self.style.ERROR(f"Failed to fetch data: {response.status_code}"))
            return

        repos = response.json()
        
        for repo in repos:
            # Skip forked repos (optional, remove if you want forks)
            if repo['fork']:
                continue
                
            name = repo['name'].replace('-', ' ').replace('_', ' ').title()
            description = repo['description'] or "No description provided."
            link = repo['html_url']
            
            # Update existing project or create a new one
            project, created = Project.objects.update_or_create(
                title=name,
                defaults={
                    'description': description,
                    'github_link': link,
                }
            )
            
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created: {name}"))
            else:
                self.stdout.write(f"Updated: {name}")

        self.stdout.write(self.style.SUCCESS("GitHub Sync Complete!"))