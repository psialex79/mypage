from django.db import models

class Follower(models.Model):
    telegram_id = models.BigIntegerField(unique=True)
    date_of_exclusion = models.DateField()
    name = models.CharField(max_length=255, blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Follower {self.telegram_id}"

