import csv
from django.core.management.base import BaseCommand
from movies.models import Actorproject

class Command(BaseCommand):
    help = 'Loading movies from a CSV file'

    def handle(self, *args, **kwargs):
        with open('Actor_project.csv', 'r') as file:
          
            reader = csv.DictReader(file)
            for row in reader:
                actorID, actorName = row['actorID'], row['actorName']
                #director, created = Director.objects.get_or_create(name=director_name)
                Actorproject.objects.get_or_create( actorID=actorID, actorName = actorName)