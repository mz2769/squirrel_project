from django.core.management.base import BaseCommand
import csv
from sightings.models import Squirrel
import datetime

class Command(BaseCommand):
    help = ("Output the specified model as CSV")
    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        f = open(csv_file, 'w+')
        writer = csv.writer(f)
        field_names = [f.name for f in Squirrel._meta.fields]
        column_names = ['X','Y','Unique Squirrel ID','Shift','Date','Age',
        'Primary Fur Color','Location','Specific Location','Running','Chasing',
        'Climbing','Eating','Foraging', 'Other Activities','Kuks',	'Quaas',
        'Moans', 'Tail flags',	'Tail twitches', 'Approaches','Indifferent','Runs from']
        writer.writerow(column_names)
        for obj in Squirrel.objects.all():
            obj.date = obj.date.strftime('%m%d%Y')
            row = [getattr(obj, field) for field in field_names]
            row[4]=obj.date
            writer.writerow(row)
        f.close()
