import random
from django.shortcuts import render
from django.contrib import messages
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
import stripe
from stripe.error import SignatureVerificationError
from .models import Reflection, GuidedReflection
from .forms import GuidedReflectionFormOne, ReflectionForm
# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY
User = get_user_model()


class ReflectionListView(LoginRequiredMixin, ListView):
    template_name= "reflections/reflections.html"

    def get_queryset(self):
        return Reflection.objects.filter(author=self.request.user)

class ReflectionCreateView(LoginRequiredMixin, CreateView):
    form_class=ReflectionForm
    template_name= "reflections/create.html"
    

    def get_form_kwargs(self):
        kwargs = super(ReflectionCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.patient = form.instance.episode_of_care.patient
        return super().form_valid(form)
    
    def get_success_url(self):
        messages.success(self.request, "Reflection Successfully created")
        return reverse("users:clinician-episode-detail", kwargs= {'pk': self.object.episode_of_care.pk})

class ReflectionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = Reflection

    def test_func(self):
        reflection = self.get_object()
        if self.request.user == reflection.author:
            return True
        return False
    
    def get_success_url(self):
        messages.error(self.request, "Reflection Deleted")
        return reverse("users:clinician-episode-detail", kwargs= {'pk': self.object.episode_of_care.pk})

class ReflectionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):


    model = Reflection
    fields = ['category', 'title', 'details']
    template_name="reflections/update.html"

    def test_func(self):
        reflection = self.get_object()
        if self.request.user == reflection.author:
            return True
        return False
    
    def get_success_url(self):
        messages.info(self.request, "Reflection Successfully Updated")
        return reverse("users:clinician-episode-detail", kwargs= {'pk': self.object.episode_of_care.pk})

class ReflectionDetailView(LoginRequiredMixin, DetailView):
    
    model= Reflection

# guided reflections

class GuidedReflectionListView(LoginRequiredMixin, ListView):
    template_name= "reflections/guided.html"

    def get_queryset(self):
        return GuidedReflection.objects.filter(author=self.request.user)

class GuidedReflectionCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):

    form_class = GuidedReflectionFormOne
    template_name= "reflections/create_guided.html"

    def get_form_kwargs(self):
        kwargs = super(GuidedReflectionCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.patient = form.instance.episode_of_care.patient
        return super().form_valid(form)
    
    def test_func(self):
        if self.request.user.access:
            return True
        return False

    def get_success_url(self):
        messages.success(self.request, "Guided Reflection Successfully created")
        return reverse("users:clinician-episode-detail", kwargs= {'pk': self.object.episode_of_care.pk})

class GuidedReflectionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = GuidedReflection

    def test_func(self):
        guided_reflection = self.get_object()
        if self.request.user == guided_reflection.author:
            return True
        return False
    
    def get_success_url(self):
        messages.error(self.request, "Guided Reflection Deleted")
        return reverse("users:clinician-episode-detail", kwargs= {'pk': self.object.episode_of_care.pk})
        
class GuidedReflectionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):


    model = GuidedReflection
    fields = ['category', 'title', 'question1', 'question2', 'question3']
    template_name="reflections/guided_update.html"

    def test_func(self):
        guided_reflection = self.get_object()
        if self.request.user == guided_reflection.author:
            return True
        return False
    
    def get_success_url(self):
        messages.info(self.request, "Guided Reflection Successfully Updated")
        return reverse("users:clinician-episode-detail", kwargs= {'pk': self.object.episode_of_care.pk})


class GuidedReflectionDetailView(LoginRequiredMixin, DetailView):
    
    model= GuidedReflection

# stripe payments below

class PaymentView(LoginRequiredMixin, TemplateView):

    template_name = "pages/upgrade.html"

    def get_context_data(self, **kwargs):
        context = super(PaymentView, self).get_context_data(**kwargs)
        context.update({
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
        })
        return context


class SuccessView(TemplateView):

    template_name="reflections/success.html"


@login_required
def stripe_checkout_session(request):

    if settings.DEBUG:
        DOMAIN = 'http://127.0.0.1:8000'

    checkout_session = stripe.checkout.Session.create(
        
        customer_email= request.user.email,
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': 1999,
                    'product_data': {
                        'name': 'Guided Reflection Tool',
                        'images': ['https://images.unsplash.com/photo-1590732879026-e89b792a84e6?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=732&q=80'],
                    },
                },
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url= DOMAIN + reverse('reflections:success'),
        cancel_url= DOMAIN + reverse('reflections:upgrade'),
    )
    return JsonResponse({ "id": checkout_session.id})




@csrf_exempt
def my_webhook_view(request):

  payload = request.body
  sig_header= request.META["HTTP_STRIPE_SIGNATURE"]
  endpoint_secret = settings.STRIPE_WEBHOOK_SECRET

  try: 
    event = stripe.Webhook.construct_event(
        payload,
        sig_header,
        endpoint_secret,
    )

  except ValueError as e:
      print(e)
      return HttpResponse(status=400)
      
  except SignatureVerificationError as e:
    # Invalid signature
    return HttpResponse(status=400)

  
  if event['type'] == 'checkout.session.completed':
    session = event['data']['object']
    print(event['data']['object']['payment_status'])
    email = session['customer_email']
    user = User.objects.get(email= email)
    user.access = True
    user.save()

    print('user given access')

  return HttpResponse(status=200)