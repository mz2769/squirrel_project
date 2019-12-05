from django.core.management.base import BaseCommand,CommandError
import csv
from sightings.models import Squirrel
import datetime

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file', nargs='+', type=str)

    def handle(self, *args, **options):
        for csv_file in options['csv_file']:
            data = csv.reader(open(csv_file), delimiter=",", quotechar='"')
            next(data)
            for row in data:
                squirrel = Squirrel()
                try:
                    squirrel.longitude = row['X']
                    squirrel.latitude = row["Y"]
                    squirrel.unique_squirrel_id = row['Unique Squirrel ID']
                    squirrel.shift = row['Shift']
                    squirrel.date = datetime.datetime.strptime(row['Date'],'%m%d%Y')
                    squirrel.age = row["Age"]
                    squirrel.primary_fur_color = row['Primary Fur Color']
                    squirrel.location = row['Location']
                    squirrel.specific_location = row['Specific Location']
                    squirrel.running = row['Running']
                    squirrel.chasing = row['Chasing']
                    squirrel.climbing = row['Climbing']
                    squirrel.eating = row['Eating']
                    squirrel.foraging = row['Foraging']
                    squirrel.other_activities = row['Other Activities']
                    squirrel.kuks = row['Kuks']
                    squirrel.quaas = row['Quaas']
                    squirrel.moans = row['Moans']
                    squirrel.tail_flags = row['Tail flags']
                    squirrel.tail_twitches = row['Tail twitches']
                    squirrel.approaches = row['Approaches']
                    squirrel.indifferent = row['Indifferent']
                    squirrel.runs_from = row['Runs from']
                except:
                    pass
                squirrel.save()
                # self.stdout.write('successfully import ')
