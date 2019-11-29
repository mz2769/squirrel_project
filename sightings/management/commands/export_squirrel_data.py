from django.core.management.base import BaseCommand
import csv
from sightings.models import Squirrel
from django.utils import encoding

class Command(BaseCommand):
    help = ("Output the specified model as CSV")
    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        f = open(csv_file, 'w+')
        writer = csv.writer(f)
        field_names = [f.name for f in Squirrel._meta.fields]
        writer.writerow(field_names)
        for obj in Squirrel.objects.all():
            row = [getattr(obj, field) for field in field_names]
            writer.writerow(row)
        f.close()
