"""Defines URL patterns for workout_logs."""

from django.urls import path

from . import views

app_name = 'workout_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    #Page that shows all workouts
    path('workouts/', views.workouts, name='workouts'),
    #Detail page for a single workout 
    path('workouts/<int:workout_id>/', views.workout, name = "workout"),
    #Page for adding a new workout
    path('new_workout/', views.new_workout, name = "new_workout"),
    #Page for adding a new entry
    path('new_entry/<int:workout_id>/', views.new_entry, name='new_entry'),
    #Page for editing any entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name = 'edit_entry')
]