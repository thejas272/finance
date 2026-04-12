from django.urls import path,re_path, include
from accounts.views import RegisterUserAPIView,AdminUserHandleAPIView


urlpatterns = [
  path("register/",RegisterUserAPIView.as_view(),name="user_registration"),
  path("users/", AdminUserHandleAPIView.as_view(), name="admin_user_management",)
]