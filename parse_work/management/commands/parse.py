import csv
from pathlib import Path

from django.core.management import BaseCommand

from parse_work.models import Temperature, Co2


class Command(BaseCommand):
    help = 'Load data from csv'

    def handle(self, *args, **options):

        # drop the data from the tables so that if we rerun the file, we don't repeat values
        Temperature.objects.all().delete()
        Co2.objects.all().delete()
        print("tables dropped successfully")
        # create table again

        # open the file to read it into the database
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(str(base_dir) + '/parse_work/data/land_ocean_temperature_index.csv', newline='') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader) # skip the header line
            for row in reader:
                print(row)

                temperature = Temperature.objects.create(
                year = int(row[0]),
                no_smoothing = float(row[1]),
                lowess = float(row[2]),
                )
                temperature.save()

        with open(str(base_dir) + '/parse_work/data/co2_mm_mlo.csv', newline='') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader)  # skip the header line
            for row in reader:
                print(row)
                temperature = Temperature()
                temperature.year = int(row[0])
                co2 = Co2.objects.create(
                year=temperature,
                month=int(row[1]),
                monthly_average=float(row[2]),
                de_season_alized=float(row[3]),
                st_dev_mon=float(row[4]),
                unc_of_mean=float(row[5]),
                )
                co2.save()

        print("data parsed successfully")
