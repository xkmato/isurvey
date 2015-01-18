import csv
import locale
from django.contrib.auth.models import User
from django.core.management import BaseCommand
from isurvey.apps.models import UserCrop

__author__ = 'awesome'


class Command(BaseCommand):
    def handle(self, *args, **options):
        f = open('crop.csv')
        spamreader = csv.reader(f, delimiter=',', quotechar='"')
        for row in spamreader:
            try:
                id, crop, crop_type, variety, crop_season, acreage_under_production, plant_spacing, input_cost, \
                annual_production, make_survey, volume_sold, volume_lost_in_PH, value_of_crop_insuared, \
                total_loan_accessed = tuple(row)

                user = User.objects.get(pk=id)
                locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )
                input_cost = locale.atof(input_cost)
                annual_production = locale.atof(annual_production)
                total_loan_accessed = locale.atof(total_loan_accessed)

                _crop = UserCrop.objects.create(user=user, crop=crop, crop_type=crop_type, variety=variety,
                                               crop_season=crop_season,
                                               acrearage_under_production=acreage_under_production,
                                               input_cost_per_acre= input_cost, annual_production=annual_production,
                                               market_supplied=make_survey, volume_sold=volume_sold,
                                               volume_lost_in_PH=volume_lost_in_PH,
                                               value_of_crop_insured=value_of_crop_insuared,
                                               total_loan_accessed=total_loan_accessed)
                print _crop
            except Exception as e:
                print e