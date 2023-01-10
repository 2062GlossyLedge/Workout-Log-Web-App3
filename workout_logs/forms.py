from django import forms

from .models import Workout, Entry

#Form for user to fill out their workout category 
class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['text']
        #Leave the label blank 
        labels = {'text': ''}

#Form for user to fill out their entry for their workout
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        #Leave the label blank
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}