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
                    squirrel.longitude = row[0]
                    squirrel.latitude = row[1]
                    squirrel.unique_squirrel_id = row[2]
                    squirrel.shift = row[4]
                    squirrel.date = datetime.datetime.strptime(row[5],'%m%d%Y')
                    squirrel.age = row[7]
                    squirrel.primary_fur_color = row[8]
                    squirrel.location = row[12]
                    squirrel.specific_location = row[14]
                    squirrel.running = row[15]
                    squirrel.chasing = row[16]
                    squirrel.climbing = row[17]
                    squirrel.eating = row[18]
                    squirrel.foraging = row[19]
                    squirrel.other_activities = row[20]
                    squirrel.kuks = row[21]
                    squirrel.quaas = row[22]
                    squirrel.moans = row[23]
                    squirrel.tail_flags = row[24]
                    squirrel.tail_twitches = row[25]
                    squirrel.approaches = row[26]
                    squirrel.indifferent = row[27]
                    squirrel.runs_from = row[28]

                except:
                    pass
                squirrel.save()
                # self.stdout.write('successfully import ')
