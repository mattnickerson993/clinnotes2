import random
from django.forms import ModelForm
from .models import GuidedReflection, Reflection
from clinnotes.users.models import EpisodeOfCare


class GuidedReflectionFormOne(ModelForm):
    

    class Meta:
        model = GuidedReflection
        fields = ['category', 'title', 'question1', 'question2', 'question3', 'episode_of_care']
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(GuidedReflectionFormOne, self).__init__(*args, **kwargs)
        self.fields['question1'].widget.attrs.update({
            'placeholder' : 'What are 3 things you could do to improve your care episode?',
            'class' :"invisible",
            'id':'guided1'
        })
        self.fields['question2'].widget.attrs.update({
            'placeholder' : "Where have you succeed thus far?",
            'class' :"invisible",
            'id':'guided2'
            })
        self.fields['question3'].widget.attrs.update({
            'placeholder' : "Whats something this patient believes to be true that isnt?",
            'class' :"invisible",
            'id':'guided3',
            })
        self.fields['question1'].label = 'Guided Question 1'
        self.fields['question2'].label = 'Guided Question 2'
        self.fields['question3'].label = 'Guided Question 3'
        
        self.fields['episode_of_care'].queryset = EpisodeOfCare.objects.filter(clinician=user)



class ReflectionForm(ModelForm):
    class Meta: 
        model = Reflection
        fields = ['category', 'title', 'details', 'episode_of_care']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(ReflectionForm, self).__init__(*args, **kwargs)
        self.fields['episode_of_care'].queryset = EpisodeOfCare.objects.filter(clinician=user)