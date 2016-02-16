from django.conf.urls import patterns, include, url
from django.contrib import admin

from djgeojson.views import TiledGeoJSONLayerView
from grazing.models import Health

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rangeland.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'grazing.views.index', name='index'),
        url(r'^allotments/(?P<allotment_unique>.*)/$', 'grazing.views.allotment', name='allotment'),
    # url(r'^data/(?P<z>\d+)/(?P<x>\d+)/(?P<y>\d+).geojson$', TiledGeoJSONLayerView.as_view(model=Health), name='data'),


    url(r'^admin/', include(admin.site.urls)),
)
