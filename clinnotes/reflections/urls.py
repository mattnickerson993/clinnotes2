from django.urls import path

from clinnotes.reflections.views import (
    ReflectionListView, 
    ReflectionCreateView,
    ReflectionDeleteView,
    ReflectionUpdateView,
    ReflectionDetailView,
    GuidedReflectionCreateView,
    GuidedReflectionDeleteView,
    GuidedReflectionUpdateView,
    GuidedReflectionListView,
    GuidedReflectionDetailView,
    PaymentView,
    stripe_checkout_session,
    SuccessView,
    my_webhook_view,
)


app_name = "reflections"
urlpatterns = [
    path("", ReflectionListView.as_view(), name="reflections"),
    path("guided/", GuidedReflectionListView.as_view(), name="reflections-guided-list"),
    path("create/", ReflectionCreateView.as_view(), name="reflections-create"),
    path("create/guided/", GuidedReflectionCreateView.as_view(), name="reflections-create-guided"),
    path("delete/<int:pk>", ReflectionDeleteView.as_view(), name="reflections-delete" ),
    path("delete/guided/<int:pk>", GuidedReflectionDeleteView.as_view(), name="reflections-guided-delete" ),
    path("update/<int:pk>",ReflectionUpdateView.as_view(), name="reflections-update"),
    path("update/guided/<int:pk>", GuidedReflectionUpdateView.as_view(), name="reflections-guided-update"),
    path("detail/<int:pk>", ReflectionDetailView.as_view(), name="reflections-detail"),
    path("detail/guided/<int:pk>", GuidedReflectionDetailView.as_view(), name="reflections-guided-detail"),
    path("upgrade/", PaymentView.as_view(), name="upgrade"),
    path("create-checkout-session/", stripe_checkout_session, name="stripe-checkout-session"),
    path("success/", SuccessView.as_view(), name="success"),
    path('webhooks/stripe/', my_webhook_view, name="stripe_webhook"),

    
]
