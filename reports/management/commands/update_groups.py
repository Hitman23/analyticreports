from django.core.management import BaseCommand
from reports.models import Group, Rapidpro_workspace


class Command(BaseCommand):
    def handle(self, *args, **options):
        Rapidpro_workspace.get_rapidpro_data()
        self.stdout.write(self.style.SUCCESS('Successfully added groups'))
