import csv
from django.core.management.base import BaseCommand
from movies.models import Featuresproject

class Command(BaseCommand):
    help = 'Loading features from a CSV file'

    def handle(self, *args, **kwargs):
        with open('Features_project.csv', 'r') as file:
          
            reader = csv.DictReader(file)
            for row in reader:
                movieID, actorID, actorRankInMovie = row['movieID'], row['actorID'], row['ranking']
                #director, created = Director.objects.get_or_create(name=director_name)
                Featuresproject.objects.get_or_create( movieID=movieID, actorID = actorID,actorRankInMovie=actorRankInMovie)