from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from accounts import serializers
from accounts.permissions import IsAdmin
from common.pagination import DefaultPagination
from accounts import models

# Create your views here.

class RegisterUserAPIView(APIView):
  permission_classes = [AllowAny]

  @swagger_auto_schema(tags=["Accounts"], request_body=serializers.UserRegisterSerializer)
  def post(self,request):

    serializer = serializers.UserRegisterSerializer(data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response("User created successfully", status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  


class AdminUserHandleAPIView(APIView):
  permission_classes = [IsAuthenticated, IsAdmin]


  @swagger_auto_schema(tags=["Admin"], request_body=serializers.AdminUserHandleSerializer)
  def post(self,request):
    serializer = serializers.AdminUserHandleSerializer(data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response("User created successfuly", status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

  @swagger_auto_schema(tags=["Admin"])
  def get(self,request):
    users = models.User.objects.all().exclude(id=request.user.id)

    paginator = DefaultPagination()
    paginated_data = paginator.paginate_queryset(users, request)

    serializer = serializers.AdminUserHandleSerializer(paginated_data, many=True)

    return paginator.get_paginated_response(serializer.data)
  


class AdminUserHandleDetailAPIView(APIView):
  permission_classes = [IsAuthenticated,IsAdmin]
  
  @swagger_auto_schema(tags=["Admin"])
  def delete(self,requesst,id):
    try:
      user = models.User.objects.get(id=id)
    except models.User.DoesNotExist:
      return Response("Invalid id, user not found.",status=status.HTTP_404_NOT_FOUND)
    
    user.is_active = False
    user.save()
    return Response("User deleted successfuly.",status=status.HTTP_200_OK)
  
  @swagger_auto_schema(tags=["Admin"], request_body=serializers.AdminUserHandleSerializer)
  def patch(self,request,id):
    try:
      user = models.User.objects.get(id=id)
    except models.User.DoesNotExist:
      return Response({"error":"Invalid user info. User not found."},status=status.HTTP_404_NOT_FOUND)
    

    serializer = serializers.AdminUserHandleSerializer(user,data=request.data,partial=True)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  


  



