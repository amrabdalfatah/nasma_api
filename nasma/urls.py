from django.urls import path, include

urlpatterns = [
    path("article/", include("article.urls")),
    path("users/", include("accounts.urls")),
    path("breathing/", include("breathing.urls")),
    path("pss/", include("pss.urls")),
    path("chatbot/", include("chatbot_api.urls")),
]