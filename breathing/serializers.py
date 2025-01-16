from rest_framework import serializers

from .models import BreathingSession, UserBreathingSession, BreathingExercise
 
class BreathingSessionSerializer(serializers.ModelSerializer):
  class Meta:
    fields = (
      "id",
      "duration",
      "date",
      "session_type",
    )
    model = BreathingSession

class UserBreathingSessionSerializer(serializers.ModelSerializer):
  class Meta:
    fields = (
      "id",
      "user_id",
      "session_id",
    )
    model = UserBreathingSession

class BreathingExerciseSerializer(serializers.ModelSerializer):
  class Meta:
    fields = (
      "id",
      "session_id",
      "duration",
      "exercise_name",
      "description",
    )
    model = BreathingExercise