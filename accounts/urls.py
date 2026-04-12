from django.urls import path,re_path, include
from accounts.views import RegisterUserAPIView,AdminUserHandleAPIView,AdminUserHandleDetailAPIView


urlpatterns = [
  path("register/",RegisterUserAPIView.as_view(),name="user_registration"),
  path("users/", AdminUserHandleAPIView.as_view(), name="admin_user_management",),
  path("users/<int:id>/",AdminUserHandleDetailAPIView.as_view(),name="admin_user_detail_management"),
]