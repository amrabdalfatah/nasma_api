from rest_framework import serializers
 
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
  class Meta:
    fields = (
      "id",
      "title",
      "content",
      "category",
    )
    model = Article