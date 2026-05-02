from rest_framework import serializers
from accounts import models as accounts_models

def get_user(request):

  if request.user.role == "viewer":
    return request.user
  
  user_id = request.query_params.get("user_id")

  if user_id is None or user_id.strip()=="":
    raise serializers.ValidationError({"error":"please give a user id."})
  
  elif not user_id.is_digit():
    raise serializers.ValidationError({"error":"please enter a valid user id."})
  
  try:
    user = accounts_models.User.objects.get(id=user_id)
  except accounts_models.User.DoesNotExist:
    raise serializers.ValidationError({"error":"user does not exist."})
  
  return user

