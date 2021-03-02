from django.db import models
from django.utils import timezone
from django.conf import settings
from clinnotes.users.models import EpisodeOfCare, Patient
# from clinnotes.users.models import User


# Create your models here.
class Reminder(models.Model):

    CATEGORY_CHOICES = [
        ('U', 'Urgent'),
        ('S', 'Soon'),
        ('E', 'Eventually'),
        ('A', 'Always'),
    ]

    author = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="reminders")
    date_posted = models.DateTimeField (default= timezone.now)
    last_edit = models.DateTimeField(auto_now = True)

    title = models.CharField(max_length=80)
    details = models.TextField()

    category = models.CharField(max_length=20, choices= CATEGORY_CHOICES, default='E')
    episode_of_care = models.ForeignKey(EpisodeOfCare, on_delete=models.CASCADE, null=True, blank=True, related_name="reminders")
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"reminder called {self.title} by {self.author} is {self.category}"