from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.conf import settings
from clinnotes.users.models import EpisodeOfCare, Patient


# Create your models here.
class Reflection(models.Model):

    CATEGORY_CHOICES = [
        ('GE', 'General'),
        ('IM', 'Areas to Improve'),
        ('SU', 'Success'),
        ('FA', 'Failure'),
        ('O', 'Other'),
    ]

    author = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="reflections")
    date_posted = models.DateTimeField (default= timezone.now)
    last_edit = models.DateTimeField(auto_now = True)

    title = models.CharField(max_length=80)
    details = models.TextField()

    category = models.CharField(max_length=20, choices= CATEGORY_CHOICES, default='GE')
    episode_of_care = models.ForeignKey(EpisodeOfCare, on_delete=models.CASCADE, null=True, blank=True, related_name="reflections")
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.title} by {self.author}"


class GuidedReflection(models.Model):

    CATEGORY_CHOICES = [
        ('GE', 'General'),
        ('IM', 'Areas to Improve'),
        ('SU', 'Success'),
        ('FA', 'Failue'),
        ('O', 'Other'),
    ]

    author = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="guided_reflections")
    date_posted = models.DateTimeField (default= timezone.now)
    last_edit = models.DateTimeField(auto_now = True)

    title = models.CharField(max_length=80)
    question1 = models.TextField()
    question2 = models.TextField()
    question3 = models.TextField()

    category = models.CharField(max_length=20, choices= CATEGORY_CHOICES, default='GE')
    episode_of_care = models.ForeignKey(EpisodeOfCare, on_delete=models.CASCADE, null=True, blank=True, related_name="guided_reflections")
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)

    