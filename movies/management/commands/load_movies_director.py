import csv
from django.core.management.base import BaseCommand
from movies.models import Directorproject

class Command(BaseCommand):
    help = 'Loading movies from a CSV file'

    def handle(self, *args, **kwargs):
        with open('Director_project.csv', 'r') as file:
          
            reader = csv.DictReader(file)
            for row in reader:
                directorID, directorName = row['directorID'], row['directorName']
                #director, created = Director.objects.get_or_create(name=director_name)
                Directorproject.objects.get_or_create( directorID=directorID, directorName = directorName)