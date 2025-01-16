from django.urls import path
from .views import UserList, UserDetail, TokenView

urlpatterns = [
  path("", UserList.as_view()),
  path("<int:pk>/", UserDetail.as_view()),
  # path("tokens/", TokenView.as_view(), name='tokens'),
]