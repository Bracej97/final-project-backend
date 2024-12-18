from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=100)
    event_description = models.CharField(max_length=500)
    event_date = models.CharField(max_length=500)
    event_start = models.CharField(max_length=50)
    event_end = models.CharField(max_length=50)
    event_attendees = models.ManyToManyField(User)
    event_location = models.CharField(max_length=300)


    def __str__(self):
        return f'{self.event_name}'

class FAQ(models.Model):
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=1000)
    category = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.question}'
