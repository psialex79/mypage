from django.db import models
from django.utils import timezone
from dateutil.relativedelta import relativedelta

class Follower(models.Model):
    telegram_id = models.BigIntegerField(unique=True)
    date_added = models.DateField(auto_now_add=True)  # Автоматическая дата добавления
    date_of_exclusion = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.pk is None and not self.date_added:
            self.date_added = timezone.now().date()
        if self.date_added:
            self.date_of_exclusion = self.date_added + relativedelta(months=+2)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Follower {self.telegram_id}"
