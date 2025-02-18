from django.contrib.auth import get_user_model
from rest_framework import generics

from .serializers import UserSerializer

class UserList(generics.ListCreateAPIView):
  queryset = get_user_model().objects.all()
  serializer_class = UserSerializer
 
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = get_user_model().objects.all()
  serializer_class = UserSerializer

class TokenView:
  pass