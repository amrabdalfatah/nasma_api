from django.urls import path

from .views import ArticleList, ArticleDetail

urlpatterns = [
  path("<int:pk>/", ArticleDetail.as_view(), name="article_detail"),
  path("", ArticleList.as_view(), name="article_list"),
]