from django.contrib.auth.models import User
from smartmin.views import SmartCRUDL, SmartListView
from isurvey.apps.models import UserProfile, UserCrop, UserLocation, PlantSpacing, CropGeoPoint

__author__ = 'awesome'


# class UserCRUDL(SmartCRUDL):
# model = User


class ProfileCRUDL(SmartCRUDL):
    model = UserProfile

    class List(SmartListView):
        search_fields = ('user__username__icontains', 'user__first_name__icontains', 'user__last_name__icontains',
                         'phone_number__icontains')


class CropCRUDL(SmartCRUDL):
    model = UserCrop

    class List(SmartListView):
        search_fields = ('user__username__icontains', 'user__first_name__icontains', 'user__last_name__icontains',
                         'crop__icontains', 'crop_type__icontains')
        link_fields = ('crop',)


class LocationCRUDL(SmartCRUDL):
    model = UserLocation


class PlantSpacingCRUDL(SmartCRUDL):
    model = PlantSpacing


class GeoPointCRUDL(SmartCRUDL):
    model = CropGeoPoint