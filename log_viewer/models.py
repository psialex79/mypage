from django.db import models

class EduLogString(models.Model):
    date = models.DateField(unique=True)

    def __str__(self):
        return f"{self.date} - {self.rate}"