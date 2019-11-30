from django.shortcuts import render, get_object_or_404
from .forms import SquirrelForm
from sightings.models import Squirrel
from django.contrib import messages

def list_sq(request):
    squirrels = Squirrel.objects.all()
    return render(request, 'sightings/list_sq.html', {'squirrels': squirrels})

def update(request,unique_squirrel_id):
    obj= get_object_or_404(Squirrel, pk=unique_squirrel_id)
    form = SquirrelForm(request.POST, instance= obj)
    context= {'form': form}
    if form.is_valid():
        obj= form.save(commit= False)
        obj.save()
        messages.success(request, "You successfully updated the squirrel")
        context= {'form': form}
        return render(request,'sightings/update.html' , context)
    else:
        form = SquirrelForm(instance= obj)
        context= {'form': form}
        return render(request,'sightings/update.html' , context)

def create(request):
    form = SquirrelForm()
    if form.is_valid():
        obj= form.save(commit= False)
        obj.save()
        messages.success(request, "You successfully added the squirrel")
        return render(request, 'sightings/create.html', {'form': form})
    else:
        context= {'form': form,
                  'error': 'The form was not updated successfully. Please enter in valid info'}
        return render(request,'sightings/create.html' , context)
