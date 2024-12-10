from getpass import getuser
from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        start_datetime = cleaned_data.get('start_datetime')
        end_datetime = cleaned_data.get('end_datetime')

        if start_datetime and end_datetime and start_datetime > end_datetime:
            raise forms.ValidationError("start time cannot be after end time.")
    class Meta:
        model = Event
        fields = ['title', 'start_datetime', 'end_datetime']

    def save(self, commit=True):
        user = getuser(self.instance)

        if not self.instance.pk:
            self.instance.created_user = user
        self.instance.updated_user = user

        instance = super(EventForm, self).save(commit=commit)

        return instance

class EventAdvancedForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        start_datetime = cleaned_data.get('start_datetime')
        end_datetime = cleaned_data.get('end_datetime')

        if start_datetime and end_datetime and start_datetime > end_datetime:
            raise forms.ValidationError("start time cannot be after end time.")
    class Meta:
        model = Event
        fields = ['title', 'start_datetime', 'end_datetime', 'description', 'place', 'repeat_options', 'attachment_files']
        exclude = ['created_time', 'created_user', 'updated_time', 'updated_user']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 20})
        }

    def save(self, commit=True):
        user = getuser(self.instance)

        if not self.instance.pk:
            self.instance.created_user = user
        self.instance.updated_user = user

        instance = super(EventAdvancedForm, self).save(commit=commit)

        return instance
