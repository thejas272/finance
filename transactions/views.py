from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from transactions import models as transactions_models
from accounts import models as accounts_models
from transactions import serializers
from common.pagination import DefaultPagination
from transactions.helpers import get_user
from django.db.models import Sum
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
  

class DashbordView(APIView):
  permission_classes = [IsAuthenticated]

  @swagger_auto_schema(tags=["Dashboard"])
  def get(self,request):

    user_instance = get_user(request)

    user_transactions = user_instance.transactions.all()

    total_credit = user_transactions.filter(type="credit").aggregate(total=Sum("amount"))["total"] or 0
    total_debit = user_transactions.filter(type="debit").aggregate(total=Sum("amount"))["total"] or 0

    balance = total_credit - total_debit

    category = user_transactions.values("category").annotate(total=Sum("amount"))

    return Response({"total_credit":total_credit,
            "total_debit":total_debit,
            "balance":balance,
            "category":category
           }, status=status.HTTP_200_OK
           )
  






      