from django.urls import path

from .views import MessageExplainerView

urlpatterns = [
  path("message-explainer/", MessageExplainerView.as_view(), name="messages"),
]