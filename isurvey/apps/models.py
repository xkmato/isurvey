from django.contrib.auth.models import User
from django.db import models

__author__ = 'awesome'


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    phone_number = models.CharField(max_length=13)
    birth_date = models.DateField()
    gender = models.CharField(choices=(('m', 'male'), ('f', 'female')), max_length=1)

    def __unicode__(self):
        return '%s' % self.user.get_full_name()


class UserLocation(models.Model):
    user = models.ForeignKey(User, related_name='locations')
    region = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    sub_county = models.CharField(max_length=30)
    parish = models.CharField(max_length=30)
    village = models.CharField(max_length=30)


class UserCrop(models.Model):
    user = models.ForeignKey(User, related_name='crops')
    crop = models.CharField(max_length=50)
    crop_type = models.CharField(max_length=50)
    variety = models.CharField(max_length=50)
    crop_season = models.CharField(max_length=100)
    acrearage_under_production = models.DecimalField(decimal_places=2, max_digits=19)
    input_cost_per_acre = models.DecimalField(decimal_places=2, max_digits=19)
    annual_production = models.DecimalField(decimal_places=2, max_digits=19)
    market_supplied = models.CharField(max_length=50)
    volume_sold = models.DecimalField(decimal_places=2, max_digits=19)
    volume_lost_in_PH = models.DecimalField(decimal_places=2, max_digits=19)
    value_of_crop_insured = models.DecimalField(decimal_places=2, max_digits=19)
    total_loan_accessed = models.DecimalField(decimal_places=2, max_digits=19)

    def __unicode__(self):
        return '%s(%s)' % (self.crop, self.crop_type)


class PlantSpacing(models.Model):
    crop = models.OneToOneField(UserCrop, related_name='plant_spacing')
    height = models.DecimalField(decimal_places=2, max_digits=19)
    width = models.DecimalField(decimal_places=2, max_digits=19)
    units = models.CharField(max_length=10)


class CropGeoPoint(models.Model):
    crop = models.ForeignKey(UserCrop, related_name='geo_points')
    accuracy = models.DecimalField(decimal_places=6, max_digits=19)
    longitude = models.DecimalField(decimal_places=6, max_digits=19)
    latitude = models.DecimalField(decimal_places=6, max_digits=19)
