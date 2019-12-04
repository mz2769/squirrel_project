from django.urls import path
from django.conf.urls import include

from . import views

app_name = 'sightings'
urlpatterns = [
    path('',views.list_sq,name='list_sq'),
    path('add/',views.create,name='create'),
    path('<unique_squirrel_id>/',views.update,name='update'),
    path('<unique_squirrel_id>/',views.delete,name='delete'),
]
