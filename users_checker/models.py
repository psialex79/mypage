from django.db import models

class Follower(models.Model):
    telegram_id = models.BigIntegerField(unique=True)
    date_of_exclusion = models.DateField()

    def __str__(self):
        return f"User {self.telegram_id}"
