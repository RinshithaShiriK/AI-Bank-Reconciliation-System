from django.db import models

class Transaction(models.Model):
    TRANSACTION_TYPE = (
        ('credit', 'Credit'),
        ('debit', 'Debit'),
    )

    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPE)
    description = models.TextField()
    source = models.CharField(max_length=20)  # bank or ledger

    def _str_(self):
        return f"{self.date} - {self.amount}"
