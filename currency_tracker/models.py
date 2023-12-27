from django.db import models

class CurrencyRate(models.Model):
    date = models.DateField(unique=True)
    rate = models.DecimalField(max_digits=10, decimal_places=4)

    def __str__(self):
        return f"{self.date} - {self.rate}"
