from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^', include('isurvey.apps.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^users/', include('smartmin.users.urls')),
)
