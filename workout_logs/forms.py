from django import forms

from .models import Workout, Entry

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}