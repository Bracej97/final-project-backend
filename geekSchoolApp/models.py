from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=100)
    event_description = models.CharField(max_length=500)
    event_in_future = models.BooleanField(default=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    event_attendees = models.ManyToManyField(User)
    event_location = models.CharField(max_length=300)
    created_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_events')
    updated_time = models.DateTimeField(auto_now=True)
    updated_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='updated_events')

    def __str__(self):
        return f'{self.event_name}'

class FAQ(models.Model):
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.question}'
