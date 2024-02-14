from django.db import models
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Follower(models.Model):
    telegram_id = models.BigIntegerField(unique=True)
    date_added = models.DateField(auto_now_add=True)  # Автоматическая дата добавления
    date_of_exclusion = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.pk:  # Если объект новый
            # Добавляем два месяца к дате добавления
            self.date_of_exclusion = self.date_added + relativedelta(months=+2)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Follower {self.telegram_id}"
