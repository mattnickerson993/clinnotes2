from datetime import date
import datetime
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class User(AbstractUser):
    """Default user for ClinNotes."""

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    access = models.BooleanField(default=False)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length= 100, blank=True)
    last_name = models.CharField(max_length= 100, blank=True)
    profession = models.CharField(max_length=100, blank=True)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")


    def __str__(self):
        return f"profile for {self.user.email}"

class Patient(models.Model):
    first_name = models.CharField(max_length= 100, blank=True)
    last_name = models.CharField(max_length= 100, blank=True)
    condition = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    treating_clinician = models.ForeignKey(User, on_delete=models.CASCADE, related_name="patients")
    next_appointment = models.DateField(blank=True, null = True, default= date.today)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class EpisodeOfCare(models.Model):

    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Discharged', 'Discharged'),
    ]
    clinician = models.ForeignKey(User, on_delete=models.CASCADE, related_name="clinician_episodes")
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="patient_episodes")
    start_date = models.DateTimeField (default= timezone.now)
    discharge_date = models.DateTimeField(null=True, blank=True, default=date.today)
    status= models.CharField(choices=STATUS_CHOICES, max_length=20, blank=True, null=True)

    def __str__(self):
        return f"patient {self.patient.first_name} {self.patient.last_name} with start date of {self.start_date.strftime('%D')}"

