from django.urls import path

from .views import BreathingExerciseView, UserBreathingSessionView, BreathingSessionView

urlpatterns = [
  path("breathingexercise/", BreathingExerciseView.as_view(), name="breathing_exercise"),
  path("userbreathingsession/", UserBreathingSessionView.as_view(), name="user_breathing_session"),
  path("breathingsession/", BreathingSessionView.as_view(), name="breathing_session"),
]