from rest_framework import generics

from .models import BreathingSession, UserBreathingSession, BreathingExercise

from .serializers import BreathingSessionSerializer, UserBreathingSessionSerializer, BreathingExerciseSerializer

# Create your views here.
class BreathingSessionView(generics.ListCreateAPIView):
  queryset = BreathingSession.objects.all()
  serializer_class = BreathingSessionSerializer

class UserBreathingSessionView(generics.ListCreateAPIView): 
  queryset = UserBreathingSession.objects.all()
  serializer_class = UserBreathingSessionSerializer


class BreathingExerciseView(generics.CreateAPIView): 
  queryset = BreathingExercise.objects.all()
  serializer_class = BreathingExerciseSerializer
