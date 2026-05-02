from django.urls import path,re_path, include
from transactions import views

urlpatterns = [
  path('', views.TransactionsView.as_view(), name="transaction"),
  path('dahsboard/', views.DashbordView.as_view(), name="dashboard"),
]