# students/management/commands/import_students.py
import csv
from django.core.management.base import BaseCommand
from movieInfoScreen.models import Movie

class Command(BaseCommand):
    help = 'Import students from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The CSV file to import')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        with open(csv_file, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Movie.objects.create(
                    movieID=row['movieID'],
                    year=row['year'],
                    title=row['title'],
                    genre=row['genre'],
                    directorName=row['directorName'],
                    imdbPictureURL=row['imdbPictureURL'],
                    rating=row['rating'],
                    tag1=row['tag1'],
                    tag2=row['tag2'],
                    tag3=row['tag3'],
                    tag4=row['tag4']
                )
        self.stdout.write(self.style.SUCCESS('Successfully imported data from %s' % csv_file))
