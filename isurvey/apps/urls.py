from isurvey.apps.views import ProfileCRUDL, CropCRUDL, LocationCRUDL, PlantSpacingCRUDL, GeoPointCRUDL

__author__ = 'awesome'

# urlpatterns = UserCRUDL().as_urlpatterns()
urlpatterns = ProfileCRUDL().as_urlpatterns()
urlpatterns += CropCRUDL().as_urlpatterns()
urlpatterns += LocationCRUDL().as_urlpatterns()
urlpatterns += PlantSpacingCRUDL().as_urlpatterns()
urlpatterns += GeoPointCRUDL().as_urlpatterns()