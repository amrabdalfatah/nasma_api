from django.contrib.auth import get_user_model
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer): # new
  class Meta:
    model = get_user_model()
    fields = ("id", "username", "email", "first_name", "last_name",)