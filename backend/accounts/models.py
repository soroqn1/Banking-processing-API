from django.db import models
from django.conf import settings

class Account(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    account_number = models.CharField(max_length=20, unique=True)

    balance=models.DecimalField(max_digits=12, decimal_places=2)
    currency=models.CharField(max_length=3, default="USD")

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.account_number} - {self.balance} - {self.currency} - {self.created_at} - {self.updated_at}"