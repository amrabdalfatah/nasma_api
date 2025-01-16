from rest_framework import generics

from .models import QustionsTest, PSSTest, PSSResult
from .serializers import QustionsTestSerializer, PSSTestSerializer, PSSResultSerializer

# Create your views here.
class QuestionsList(generics.ListAPIView):
  queryset = QustionsTest.objects.all()
  serializer_class = QustionsTestSerializer

class QuestionDetail(generics.RetrieveAPIView): 
  queryset = QustionsTest.objects.all()
  serializer_class = QustionsTestSerializer

class PSSTestList(generics.ListAPIView): 
  queryset = PSSTest.objects.all()
  serializer_class = PSSTestSerializer

class PSSTestDetail(generics.CreateAPIView): 
  queryset = PSSTest.objects.all()
  serializer_class = PSSTestSerializer

class PSSResultList(generics.ListCreateAPIView): 
  queryset = PSSResult.objects.all()
  serializer_class = PSSResultSerializer
