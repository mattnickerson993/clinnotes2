from django.urls import path

from clinnotes.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
    EpisodeListView,
    EpisodeCreateView,
    EpisodeDetailView,
    EpisodeDeleteView,
    EpisodeUpdateView,
    PatientListView,
    PatientCreateView,
    PatientDetailView,
    PatientDeleteView,
    PatientUpdateView,
)
from . import views

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("profile/",views.profile, name="profile" ),
    path("clinician/", EpisodeListView.as_view(), name="clinician-episodes"),
    path("clinician/episode/create", EpisodeCreateView.as_view(), name="clinician-episode-create"),
    path("clinician/episode/delete/<int:pk>", EpisodeDeleteView.as_view(), name="clinician-episode-delete"),
    path("clinician/episode/update/<int:pk>", EpisodeUpdateView.as_view(), name="clinician-episode-update"),
    path("clinician/episode/detail/<int:pk>", EpisodeDetailView.as_view(), name="clinician-episode-detail"),
    path("clinician/patient/create", PatientCreateView.as_view(), name="clinician-patient-create"),
    path("clinician/patient/delete/<int:pk>", PatientDeleteView.as_view(), name="clinician-patient-delete"),
    path("clinician/patient/update/<int:pk>", PatientUpdateView.as_view(), name="clinician-patient-update"),
    path("clinician/patient/detail/<int:pk>", PatientDetailView.as_view(), name="clinician-patient-detail"),

    path("<str:username>/", view=user_detail_view, name="detail"),
    
]
