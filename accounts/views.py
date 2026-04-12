from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from accounts import serializers
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
  


