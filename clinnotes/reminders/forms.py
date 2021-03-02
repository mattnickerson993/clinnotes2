from django import forms
from .models import Reminder
from clinnotes.users.models import EpisodeOfCare


class ReminderForm(forms.ModelForm):
    class Meta: 
        model = Reminder
        fields = ['category', 'title', 'details', 'episode_of_care']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(ReminderForm, self).__init__(*args, **kwargs)
        self.fields['episode_of_care'].queryset = EpisodeOfCare.objects.filter(clinician=user)