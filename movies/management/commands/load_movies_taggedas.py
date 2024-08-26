import csv
from django.core.management.base import BaseCommand
from movies.models import Taggedasproject

class Command(BaseCommand):
    help = 'Loading taggedas features from a CSV file'

    def handle(self, *args, **kwargs):
        with open('TaggedAs_project.csv', 'r') as file:
          
            reader = csv.DictReader(file)
            for row in reader:
                movieID, tagID, tagweight = row['movieID'], row['tagID'], row['tagWeight']
                #director, created = Director.objects.get_or_create(name=director_name)
                Taggedasproject.objects.get_or_create( movieID=movieID, tagID = tagID,tagweight=tagweight)