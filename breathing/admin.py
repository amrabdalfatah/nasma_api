from django.contrib import admin
from .models import BreathingSession, UserBreathingSession, BreathingExercise

# Register your models here.
admin.site.register(BreathingSession)
admin.site.register(UserBreathingSession)
admin.site.register(BreathingExercise)
