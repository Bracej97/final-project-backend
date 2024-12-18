from rest_framework import serializers
from geekSchoolApp.models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'event_name',
            'event_description',
            'event_date',
            'event_start',
            'event_end',
            'event_attendees',
            'event_location'
            ]
