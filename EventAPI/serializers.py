from rest_framework import serializers
from geekSchoolApp.models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'event_name',
            'event_description',
            'event_in_future',
            'start_datetime',
            'end_datetime',
            'event_attendees',
            'event_location',
            'created_user',
            'updated_time',
            'updated_user'
            ]
