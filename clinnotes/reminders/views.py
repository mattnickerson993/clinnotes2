from django.shortcuts import render
from django.contrib import messages
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from .models import Reminder
from .forms import ReminderForm
# Create your views here.


class ReminderListView(LoginRequiredMixin, ListView):
    template_name= "reminders/reminders.html"

    def get_queryset(self):
        return Reminder.objects.filter(author=self.request.user).order_by('-category')

class ReminderCreateView(LoginRequiredMixin, CreateView):
    form_class= ReminderForm
    template_name= "reminders/create.html"

    def get_form_kwargs(self):
        kwargs = super(ReminderCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.patient = form.instance.episode_of_care.patient
        return super().form_valid(form)
   
    def get_success_url(self):
        messages.success(self.request, "Reminder Successfully created")
        return reverse("users:clinician-episode-detail", kwargs= {'pk': self.object.episode_of_care.pk})

   

    

class ReminderDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = Reminder
    success_url = '/reminders/'

    def test_func(self):
        reminder = self.get_object()
        if self.request.user == reminder.author:
            return True
        return False
    
    def get_success_url(self):
        messages.error(self.request, "Reminder Deleted")
        return reverse("users:clinician-episode-detail", kwargs= {'pk': self.object.episode_of_care.pk})

class ReminderUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):


    model = Reminder
    fields = ['category', 'title', 'details']
    success_url = '/reminders/'
    template_name="reminders/update.html"

    def test_func(self):
        reminder = self.get_object()
        if self.request.user == reminder.author:
            return True
        return False
    
    def get_success_url(self):
        messages.info(self.request, "Reminder Successfully Updated")
        return reverse("users:clinician-episode-detail", kwargs= {'pk': self.object.episode_of_care.pk})

class ReminderDetailView(LoginRequiredMixin, DetailView):
    
    model= Reminder