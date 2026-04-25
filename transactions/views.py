from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from transactions import models as transactions_models
from transactions import serializers
from common.pagination import DefaultPagination
# Create your views here.



class TransactionsView(APIView):
  permission_classes = [IsAuthenticated]

  def get_queryset(self, request):
    if request.user.role == "viewer":
      return transactions_models.TransactionsModel.objects.filter(user=request.user)
    return transactions_models.TransactionsModel.objects.all()

  @swagger_auto_schema(tags=["Transactions"])
  def get(self, request):
    transactions = self.get_queryset(request)

    paginator = DefaultPagination()
    paginated_data = paginator.paginate_queryset(transactions, request)

    serializer = serializers.TransactionSerializer(paginated_data, many=True)

    return paginator.get_paginated_response(serializer.data)