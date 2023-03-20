#This model tells Django how to work with the data on the Workouts and its entries
from django.db import models
from django.contrib.auth.models import User #authentication system 

class  Workout(models.Model):
    """A Workout the user is focusing on."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE) #established a relationship between user and and model using a foreign key, 
    #such that the user's topics would be deleted if the user was deleted

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Entry(models.Model):
    """The workout name along with the weight and sets/reps done."""
    #This is a foreign key (ID) instance that connects each entry to its workout key. 
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    text = models.TextField()#null=True)
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

       