from django.urls import path
from django.conf.urls import include

from . import views

app_name = 'sightings'
urlpatterns = [
    path('map/',views.map,name='map'),
    path('sightings/',views.list_sq,name='list_sq'),
    path('sightings/add/',views.create,name='create'),
    path('sightings/stats/',views.stats,name='stats'),
    path('sightings/<unique_squirrel_id>/',views.update,name='update'),
]
