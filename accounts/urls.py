from django.urls import path,re_path, include
from accounts.views import RegisterUserAPIView


urlpatterns = [
  path("register/",RegisterUserAPIView.as_view(),name="user_registration"),
]