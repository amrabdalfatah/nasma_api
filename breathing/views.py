from rest_framework import generics

from .models import BreathingSession, UserBreathingSession, BreathingExercise

from .serializers import BreathingSessionSerializer, UserBreathingSessionSerializer, BreathingExerciseSerializer

# Create your views here.
class BreathingSessionView(generics.CreateAPIView):
  queryset = BreathingSession.objects.all()
  serializer_class = BreathingSessionSerializer

class UserBreathingSessionView(generics.CreateAPIView): 
  queryset = UserBreathingSession.objects.all()
  serializer_class = UserBreathingSessionSerializer

class BreathingExerciseView(generics.CreateAPIView): 
  queryset = BreathingExercise.objects.all()
  serializer_class = BreathingExerciseSerializer
