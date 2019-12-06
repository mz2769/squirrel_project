from django.core.management.base import BaseCommand,CommandError
import csv
from sightings.models import Squirrel
import datetime

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)
            for row in data:
                row['Date']=datetime.datetime.strptime(row['Date'],'%m%d%Y')
                squirrel = Squirrel()

                try:
                    squirrel.latitude = row['X']
                    squirrel.longitude = row["Y"]
                    squirrel.unique_squirrel_id = row['Unique Squirrel ID']
                    squirrel.shift = row['Shift']
                    squirrel.date = row['Date']
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
