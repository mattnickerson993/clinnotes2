from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django import forms
from .models import Profile, Patient, EpisodeOfCare

User = get_user_model()


class UserChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(admin_forms.UserCreationForm):
    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields= ('first_name', 'last_name', 'profession', 'image',)

class EpisodeForm(forms.ModelForm):
    class Meta: 
        model = EpisodeOfCare
        fields = ['patient', 'start_date', 'status']

    def __init__(self, *args, **kwargs):
        print(kwargs)
        user = kwargs.pop('user')
        print(user)
        super(EpisodeForm, self).__init__(*args, **kwargs)
        self.fields['patient'].queryset = Patient.objects.filter(treating_clinician=user)