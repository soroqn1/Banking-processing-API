from django.db import models
from django.conf import settings
from accounts.models import Account

class Transaction(models.Model):
    TRANSACTION_TYPE = [
        ('deposit', 'Deposit'),
        ('withdraw', 'Withdraw'),
        ('transfer', 'Transfer'),
    ]
    
    sender = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='sent_transactions', null=True, blank=True)
    receiver = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='received_transactions', null=True, blank=True)

    amount = models.DecimalField(max_digits=12, decimal_places=2)
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)