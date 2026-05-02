from django.contrib import admin
from transactions import models as transactions_models
# Register your models here.

@admin.register(transactions_models.TransactionsModel)
class TransactionAdmin(admin.ModelAdmin):
  list_display = ["user","type","amount","is_active"]
  list_filter = ["is_active","type"]
  