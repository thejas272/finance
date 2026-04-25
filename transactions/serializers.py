from rest_framework import serializers
from transactions import models

class TransactionSerializer(serializers.ModelSerializer):

  class Meta:
    model = models.TransactionsModel
    fields = "__all__"

    