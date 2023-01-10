from django.contrib import admin

from .models import Workout, Entry

#Have these modules be added to the admin site 
admin.site.register(Workout)
admin.site.register(Entry)