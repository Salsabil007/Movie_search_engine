import csv
from django.core.management.base import BaseCommand
from movies.models import Movie2

class Command(BaseCommand):
    help = 'Load movies from CSV file'

    def handle(self, *args, **kwargs):
        with open('movies2.csv', 'r') as file:
            #reader = csv.reader(file)
            reader = csv.DictReader(file)
            for row in reader:
                director_name, movie_title = row['director'], row['movie']
                #director, created = Director.objects.get_or_create(name=director_name)
                Movie2.objects.get_or_create(title=movie_title, director=director_name)

        with open('rating.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                movie_title, imdb_rating = row['movie'],row['rating']
                try:
                    movie = Movie2.objects.get(title=movie_title)
                    movie.imdb_rating = float(imdb_rating)
                    movie.save()
                except movie.DoesNotExist:
                    self.stdout.write(self.style.WARNING(f'Movie "{movie_title}" not found.'))
