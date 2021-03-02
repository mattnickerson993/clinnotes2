from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView, CreateView, ListView, DeleteView
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm, EpisodeForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import EpisodeOfCare, Patient

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = User
    fields = ["name"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()

@login_required
def profile(request):
    user = User.objects.get(email = request.user.email)
    if request.method == "POST":
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance = user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.info(request, f'profile for {user.profile.first_name} updated')
            return redirect('users:profile')
    else:
        
        profile_form = ProfileUpdateForm(instance = user.profile)

    return render(request, "users/profile.html", {
        "form": profile_form,
    })


# episodes of care CRUD

class EpisodeListView(LoginRequiredMixin, ListView):
    template_name= "clinicians/clinician.html"

    def get_queryset(self):
        return EpisodeOfCare.objects.filter(clinician=self.request.user)

class EpisodeCreateView(LoginRequiredMixin, CreateView):
    form_class= EpisodeForm
    template_name= "clinicians/episode_create.html"
    success_url= '/users/clinician/'

    def get_form_kwargs(self):
        kwargs = super(EpisodeCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.clinician = self.request.user
        messages.success(self.request, "Episode Successfully Created")
        return super().form_valid(form)

class EpisodeDetailView(LoginRequiredMixin, DetailView):

    model=EpisodeOfCare
    template_name = "clinicians/episode_detail.html"

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        episode=self. get_object()
        context['reminders'] = episode.reminders.all().order_by('-category')
        context['reflections'] = episode.reflections.all().order_by('-date_posted')
        context['guided_reflections'] = episode.guided_reflections.all().order_by('-date_posted')
        context['access']=episode.clinician.access
        return context

class EpisodeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model= EpisodeOfCare
    template_name = 'clinicians/episode_confirm_delete.html'
    
    def test_func(self):
        episode = self.get_object()
        if self.request.user == episode.clinician:
            return True
        return False

    def get_success_url(self):
        messages.error(self.request, "Episode Deleted")
        return reverse("users:clinician-episodes")

class EpisodeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = EpisodeOfCare
    fields = ['start_date', 'status']
    template_name = 'clinicians/episode_update.html'


    def test_func(self):
        episode = self.get_object()
        if self.request.user == episode.clinician:
            return True
        return False

    def get_success_url(self):
        messages.info(self.request, "Episode Successfully Updated")
        return reverse("users:clinician-episodes")

# Patient CRUD

class PatientListView(LoginRequiredMixin, UserPassesTestMixin, ListView):

    def get_queryset(self):
        return Patient.objects.all()

class PatientCreateView(LoginRequiredMixin, CreateView):

    model = Patient
    fields = ["first_name", "last_name", "condition", "email", "notes"]
    template_name = "clinicians/patient_create.html"

    def form_valid(self, form):
        form.instance.treating_clinician = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, "Patient Successfully Created")
        return reverse("users:clinician-episodes")

class PatientDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = Patient
    template_name = 'clinicians/patient_confirm_delete.html'
    

    def test_func(self):
        patient = self.get_object()
        if self.request.user == patient.treating_clinician:
            return True
        return False

    def get_success_url(self):
        messages.error(self.request, "Episode Deleted")
        return reverse("users:clinician-episodes")

class PatientUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Patient
    template_name = "clinicians/patient_update.html"
    fields = ["first_name", "last_name", "condition", "email", "notes"]

    def test_func(self):
        patient = self.get_object()
        if self.request.user == patient.treating_clinician:
            return True
        return False

    def get_success_url(self):
        messages.info(self.request, "Patient Successfully Updated")
        return reverse("users:clinician-episodes")

class PatientDetailView(LoginRequiredMixin, DetailView):

    model=Patient
    template_name = "clinicians/patient_detail.html"