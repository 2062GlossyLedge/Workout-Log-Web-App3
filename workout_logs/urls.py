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
    path('new_workout/', views.new_workout, name = "new_workout")
]