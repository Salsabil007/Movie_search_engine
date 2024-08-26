import csv
from django.core.management.base import BaseCommand
from movieInfoScreen.models import testrun

class Command(BaseCommand):
    # help = 'Import students from a CSV file'

    #def add_arguments(self, parser):
     #   parser.add_argument('csv_file', type=str, help='The CSV file to import')

    def handle(self, *args, **kwargs):
        try:
            with open('testrun.csv', 't') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    movieID, year, title, genre, directorName = row['movieID'], row['year'], row['title'], row['genre'], row['directorName']

            self.stdout.write(self.style.SUCCESS('Successfully imported data from %s'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('File "%s" not found'))
        except Exception as e:
            self.stdout.write(self.style.ERROR('An error occurred: %s' % str(e)))                
