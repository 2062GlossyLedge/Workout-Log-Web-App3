#Defines all the html templates that will be viewed as well as how the data will be structured by using queries 
from django.shortcuts import render, redirect

from .models import Workout
from .forms import WorkoutForm

# Create your views here.
def index(request):
    """The home page for Workout Log."""
    return render(request, 'workout_logs/index.html')

def workouts(request):
    """Show all workouts."""
    workouts = Workout.objects.order_by('date_added')
    context = {'workouts': workouts}
    return render(request, 'workout_logs/workouts.html', context)

def workout(request, workout_id):
    """Show a single workout, and all its entries."""
    workout = Workout.objects.get(id=workout_id)
    entries = workout.entry_set.order_by('-date_added')
    context = {'workout': workout, 'entries': entries}
    return render(request, 'workout_logs/workout.html', context)

    #@login_required
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
    #Display a blank or invalid form 
    context = {'form': form}
    return render(request, 'workout_logs/new_workout.html', context)

# @login_required
# def new_entry(request, workout_id):
#     """Add a new entry for a particular workout."""
#     workout = workout.objects.get(id=workout_id)
#     if workout.owner != request.user:
#         raise Http404
    
#     if request.method != 'POST':
#         # No data submitted; create a blank form.
#         form = EntryForm()        
#     else:
#         # POST data submitted; process data.
#         form = EntryForm(data=request.POST)
#         if form.is_valid():
#             new_entry = form.save(commit=False)
#             new_entry.workout = workout
#             new_entry.save()
#             return HttpResponseRedirect(reverse('workout_logs:workout',
#                                         args=[workout_id]))
    
#     context = {'workout': workout, 'form': form}
#     return render(request, 'workout_logs/new_entry.html', context)

# @login_required
# def edit_entry(request, entry_id):
#     """Edit an existing entry."""
#     entry = Entry.objects.get(id=entry_id)
#     workout = entry.workout
#     if workout.owner != request.user:
#         raise Http404
    
#     if request.method != 'POST':
#         # Initial request; pre-fill form with the current entry.
#         form = EntryForm(instance=entry)
#     else:
#         # POST data submitted; process data.
#         form = EntryForm(instance=entry, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('workout_logs:workout',
#                                         args=[workout.id]))
    
#     context = {'entry': entry, 'workout': workout, 'form': form}
#     return render(request, 'workout_logs/edit_entry.html', context)