from django.db import models

class CurrencyRate(models.Model):
    date = models.DateField(unique=True)
    rate = models.DecimalField(max_digits=10, decimal_places=4)

    def __str__(self):
        return f"{self.date} - {self.rate}"

class CurrencyPurchase(models.Model):
    date = models.DateField(verbose_name="Дата покупки")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма в долларах")
    rate = models.DecimalField(max_digits=10, decimal_places=4, verbose_name="Курс обмена")

    def __str__(self):
        return f"Покупка {self.amount} USD на {self.date}"
