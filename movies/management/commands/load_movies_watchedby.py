import csv
from django.core.management.base import BaseCommand
from movies.models import Watchedbyproject

class Command(BaseCommand):
    help = 'Loading watchedby features from a CSV file'

    def handle(self, *args, **kwargs):
        with open('Watchedby_project.csv', 'r') as file:
          
            reader = csv.DictReader(file)
            for row in reader:
                movieID, userID, rating = row['movieID'], row['userID'], row['rating']
                #director, created = Director.objects.get_or_create(name=director_name)
                Watchedbyproject.objects.get_or_create( movieID=movieID, userID = userID,rating=rating)