from django.conf import settings
from django.db import models


class BreathingSession(models.Model):
  duration = models.IntegerField()
  date = models.DateTimeField(auto_now_add=True)
  session_type = models.CharField(max_length=30)

  def __str__(self):
    return self.session_type
  

# Create your models here.
class UserBreathingSession(models.Model):
  user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  session_id = models.ForeignKey(BreathingSession, on_delete=models.CASCADE)
  

class BreathingExercise(models.Model):
  session_id = models.ForeignKey(BreathingSession, on_delete=models.CASCADE)
  duration = models.IntegerField()
  exercise_name = models.CharField(max_length=50)
  description = models.CharField(max_length=200)
  
  def __str__(self):
    return self.exercise_name