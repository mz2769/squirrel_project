from django.shortcuts import render, get_object_or_404
from .forms import SquirrelForm
from sightings.models import Squirrel
from django.contrib import messages

def list_sq(request):
    squirrels = Squirrel.objects.all()
    return render(request, 'sightings/list_sq.html', {'squirrels': squirrels})

def map(request):
    squirrels = Squirrel.objects.all()
    return render(request, 'squirrel/map.html', {'squirrels': squirrels})

def create(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            obj= form.save(commit= False)
            obj.save()
            messages.success(request, "You have successfully added the squirrel sighting")
            return render(request, 'sightings/create.html', {'form': form})
        else:
            context= {'form': form,
                      'error': 'The form was not added successfully. Please enter in valid info'}
            return render(request,'sightings/create.html' , context)
    else:
        form=SquirrelForm()
        return render(request, 'sightings/create.html', {'form': form})

def update(request,unique_squirrel_id,del=False):
    if del=False:
        obj= get_object_or_404(Squirrel, pk=unique_squirrel_id)
        if request.method == 'POST':
            form = SquirrelForm(request.POST, instance= obj)
            context= {'form': form}
            if form.is_valid():
                obj= form.save(commit= False)
                obj.save()
                messages.success(request, "You have successfully updated the squirrel sighting")
                context= {'form': form}
                return render(request,'sightings/update.html' , context)
            else:
                context= {'form': form,
                          'error': 'The form was not updated successfully. Please enter in valid info'}
                return render(request,'sightings/update.html' , context)
        else:
            form = SquirrelForm(instance= obj)
            return render(request,'sightings/update.html' , {'form': form})


    else:
        obj= get_object_or_404(Squirrel, pk=unique_squirrel_id)
        # form = SquirrelForm(request.POST, instance= obj)
        # context= {'form': form}
        obj.delete()
        messages.success(request, "You have successfully deleted the squirrel sighting")
