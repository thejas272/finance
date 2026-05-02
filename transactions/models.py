from django.db import models
import accounts.models as accounts_models
# Create your models here.

class TransactionsModel(models.Model):
  TYPE_CHOICES = [("credit","Credit"),
                  ("debit","Debit"),
                 ]
  
  CATEGORY_CHOICES = [('salary','Salary'),
                      ('rent','Rent'),
                      ('food','Food')
                     ]
  user = models.ForeignKey(accounts_models.User, related_name="transactions" ,on_delete=models.SET_NULL, null=True, blank=True)
  amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
  category = models.CharField(null=True, blank=True, choices=CATEGORY_CHOICES)
  type = models.CharField(null=False, blank=False, choices=TYPE_CHOICES, max_length=50)
  purpose = models.TextField(null=True, blank=True)

  is_active = models.BooleanField(default=True)
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name = "Transaction"
    verbose_name_plural = "Transactions"