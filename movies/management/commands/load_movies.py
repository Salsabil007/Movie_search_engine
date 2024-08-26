import csv
from django.core.management.base import BaseCommand
from movies.models import Director, Movie

class Command(BaseCommand):
    help = 'Load movies from CSV file'

    def handle(self, *args, **kwargs):
        with open('movies.csv', 'r') as file:
            #reader = csv.reader(file)
            reader = csv.DictReader(file)
            for row in reader:
                director_name, movie_title = row['director'], row['movie']
                director, created = Director.objects.get_or_create(name=director_name)
                Movie.objects.get_or_create(title=movie_title, director=director)
