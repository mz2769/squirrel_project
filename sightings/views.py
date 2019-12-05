from django.shortcuts import render, get_object_or_404,shortcuts
from .forms import SquirrelForm
from sightings.models import Squirrel
from django.contrib import messages

def list_sq(request):
    squirrels = Squirrel.objects.all()
    return render(request, 'sightings/list_sq.html', {'squirrels': squirrels})

def map(request):
    sightings = Squirrel.objects.all()
    return render(request, 'sightings/map.html', {'sightings': sightings})

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

def update(request,unique_squirrel_id):
    obj= get_object_or_404(Squirrel, pk=unique_squirrel_id)
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance= obj)
        if form.is_valid():
            # obj= form.save(commit= False)
            # obj.save()
            form.save()
            messages.success(request, "You have successfully updated the squirrel sighting")
            return redirect('/sightings/{unique_squirrel_id}')
        else:
            context= {'form': form,
                      'error': 'The form was not updated successfully. Please enter in valid info'}
    else:
        form = SquirrelForm(instance= obj)
        context= {'form': form}
    return render(request,'sightings/update.html' , context)

def stats(request):
    squirrels = Squirrel.objects.all()
