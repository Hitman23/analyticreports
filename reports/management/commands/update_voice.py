from django.core.management import BaseCommand

from reports.models import Voice, Project


class Command(BaseCommand):
    def handle(self, *args, **options):
        Project.get_project_voice_data()

        self.stdout.write(self.style.SUCCESS('Successfully added voice data'))
