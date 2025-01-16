from rest_framework import views, status
from rest_framework.response import Response

from .serializers import MessageExplainerSerializer
from .models import MessageExplainer


class MessageExplainerView(views.APIView):
  # queryset = MessageExplainer.objects.all()
  serializer_class = MessageExplainerSerializer

  def get(self, request, format=None):
    pass

  def post(self, request, format=None):
    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)