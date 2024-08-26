import csv
from django.core.management.base import BaseCommand
from movies.models import Taggedasproject, Tagproject

class Command(BaseCommand):
    help = 'Loading tags from a CSV file'

    def handle(self, *args, **kwargs):
        with open('Tag_project.csv', 'r') as file:
          
            reader = csv.DictReader(file)
            for row in reader:
                tagID, tagName = row['id'], row['value']
                #director, created = Director.objects.get_or_create(name=director_name)
                Tagproject.objects.get_or_create( tagID=tagID, tagName = tagName)