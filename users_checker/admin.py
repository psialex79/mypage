from django.contrib import admin
from .models import Follower

@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    list_display = ['telegram_id', 'date_of_exclusion']
