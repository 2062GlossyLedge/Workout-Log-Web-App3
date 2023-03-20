#Defines all the html templates that will be viewed as well as how the data will be structured by using queries 
from django.shortcuts import render, redirect

from .models import Workout, Entry
from .forms import WorkoutForm, EntryForm
# from django.http import HttpResponseRedirect, Http404
# from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    """The home page for Workout Log."""
    return render(request, 'workout_logs/index.html')

@login_required #checks if user is logged in before running workouts()
def workouts(request):
    """Show all workouts."""
    workouts = Workout.objects.order_by('date_added')
    context = {'workouts': workouts}
    return render(request, 'workout_logs/workouts.html', context)

@login_required
def workout(request, workout_id):
    """Show a single workout, and all its entries."""
    workout = Workout.objects.get(id=workout_id)#, null=True)
    entries = workout.entry_set.order_by('-date_added')
    context = {'workout': workout, 'entries': entries}
    return render(request, 'workout_logs/workout.html', context)

@login_required
def new_workout(request):
    """Add a new workout."""
    #When user sends data in a form, use a post request 
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = WorkoutForm()
    else:
        # POST data submitted; process data.
        form = WorkoutForm(request.POST)
        if form.is_valid(): 
            form.save()
            #new_workout = form.save(commit=False)
            #new_workout.owner = request.user
            #return user back to view of all workouts after making their workout entry 
            return redirect('workout_logs:workouts')
            #return HttpResponseRedirect(reverse('workout_logs:workouts'))
    #create a context dictionary and render page for a blank form or an invalid form     context = {'form': form}
    return render(request, 'workout_logs/new_workout.html', context)

@login_required
def new_entry(request, workout_id):
    """Add a new entry for a particular workout."""
    workout = Workout.objects.get(id=workout_id)
    # if workout.owner != request.user:
    #     raise Http404
    
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()        
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            #creates a "new_entry object and assign it to new_entry without saving it to the database yet"
            new_entry = form.save(commit=False)
            #Save the correct workout to the database 
            new_entry.workout = workout
            #fixed from ChatGPT 
            #new_entry.Workout_id = workout.id
            new_entry.save()
            return redirect('workout_logs:workout', workout_id=workout_id)
            #return HttpResponseRedirect(reverse('workout_logs:workout',
                                        #args=[workout_id]))
    #create a context dictionary and render page for a blank form or an invalid form 
    context = {'workout': workout, 'form': form}
    return render(request, 'workout_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    #retrieve entry_id from database 
    entry = Entry.objects.get(id=entry_id)
    workout = entry.workout
    # if workout.owner != request.user:
    #     raise Http404
    
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            #call save now because "the entry is already associated with the correct topic" (pg.419)
            form.save()
            #goes back to workout page that should show updated entry 
            return redirect('workout_logs:workout', workout_id=workout.id)
            # return HttpResponseRedirect(reverse('workout_logs:workout',
            #                             args=[workout.id]))
    
    #create a context dictionary and render page for a blank form or an invalid form 
    context = {'entry': entry, 'workout': workout, 'form': form}
    return render(request, 'workout_logs/edit_entry.html', context)