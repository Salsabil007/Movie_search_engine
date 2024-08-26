import csv
from django.core.management.base import BaseCommand
from movies.models import Movieproject

class Command(BaseCommand):
    help = 'Loading movies from a CSV file'

    def handle(self, *args, **kwargs):
        with open('Movie_project.csv', 'r') as file:
         
            reader = csv.DictReader(file)
            for row in reader:
                movieID,imdbPictureURL,year,title, genre, AddressSpace1, AddressSpace2,directorID = row['movieID'], row['imdbPictureURL'], row['year'],row['title'],row['genre'],row['location1'], row['location2'], row['directorID']
                #director, created = Director.objects.get_or_create(name=director_name)
                Movieproject.objects.get_or_create(movieID=movieID,imdbPictureURL=imdbPictureURL,year=year, title=title,genre=genre,AddressSpace1=AddressSpace1,AddressSpace2=AddressSpace2, directorID=directorID)