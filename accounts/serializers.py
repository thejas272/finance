from rest_framework import serializers
from accounts import models

class UserRegisterSerializer(serializers.ModelSerializer):

  first_name = serializers.CharField(required=True,max_length = 100)
  last_name = serializers.CharField(required=True, max_length = 100)
  username  = serializers.CharField(required=True, max_length = 100)
  password  = serializers.CharField(required=True, max_length = 100, write_only=True)
  email     = serializers.CharField(max_length=100, required=True)

  class Meta:
    model = models.User
    fields = ["first_name","last_name","username","email","password"]

  def validate_username(self,value):
    if models.User.objects.filter(username=value).exists():
      raise serializers.ValidationError("Username already exists.")
    return value
  
  def validate_email(self,value):
    if models.User.objects.filter(email=value).exists():
      raise serializers.ValidationError("Email already exists.")
    return value
  
  def create(self, validated_data):
    user = models.User.objects.create_user(**validated_data)
    user.set_password(validated_data["password"])
    user.save()
    return user
  


class AdminUserHandleSerializer(serializers.ModelSerializer):

  class Meta:
    model = models.User
    fields = "__all__"
    extra_kwargs = {
      "password":{"write_only":True}
    }
    read_only_fields = ["last_login","date_joined"]

  
  def create(self, validated_data):
    user = models.User.objects.create_user(**validated_data)
    user.set_password(validated_data["password"])
    user.save()
    return user
