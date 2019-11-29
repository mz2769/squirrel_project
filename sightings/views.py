from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from sightings.models import Squirrel

def list_sq(request):
    squirrels = Squirrel.objects.all()
    return render(request, 'sightings/list_sq.html', {'squirrels': squirrels})





# class squirrellist(generic.ListView):
#     model = Squirrel
#     template_name = 'squirrel/sightings.html'


# def update_sightings(request,pk):
#     sighting = Squirrel.objects.get(pk=unique_squirrel_id)
#     if request.method == 'POST':
#         form = SquirrelForm(request.POST, instance=sighting)
#         if sighting.is_valid():
#
            # form.save()


# class SquirrelAdd(CreateView):
#     model = Squirrel
#     fields = '__all__'
