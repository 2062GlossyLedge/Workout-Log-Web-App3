#This model tells Django how to work with the data on the Workouts and its entries
from django.db import models

class  Workout(models.Model):
    """A Workout the user is focusing on."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Entry(models.Model):
    """The workout name along with the weight and sets/reps done."""
    Workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries'
 
    def __str__(self):
        """Return a string representation of the model."""
        #Give ellipses for an entry if it's longer than 50 chars
        if(self.text.__len__() > 50):
            return self.text[:50] + "..."
        else:
            return self.text

            #change