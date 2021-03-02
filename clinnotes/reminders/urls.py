
from django.urls import path

from clinnotes.reminders.views import (
    ReminderListView, 
    ReminderCreateView,
    ReminderDeleteView,
    ReminderUpdateView,
    ReminderDetailView,
)
from . import views

app_name = "reminders"
urlpatterns = [
    path("", ReminderListView.as_view(), name="reminders"),
    path("create/", ReminderCreateView.as_view(), name="reminders-create"),
    path("delete/<int:pk>", ReminderDeleteView.as_view(), name="reminders-delete" ),
    path("update/<int:pk>",ReminderUpdateView.as_view(), name="reminders-update"),
    path("detail/<int:pk>", ReminderDetailView.as_view(), name="reminders-detail"),
    
]