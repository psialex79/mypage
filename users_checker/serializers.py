from rest_framework import serializers
from .models import Follower

class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ['telegram_id', 'name', 'note']  # Убрали 'date_of_exclusion'
