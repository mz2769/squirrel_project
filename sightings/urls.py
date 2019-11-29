from django.urls import path

from . import views

app_name = 'sightings'
urlpatterns = [
path('',views.list_sq,name='list_sq'),#list all squirrels with links
# path('<unique_squirrel_id>/',views.),
# path('add/',),
# path('<unique_squirrel_id>/',),
# path('stats/',),
]
