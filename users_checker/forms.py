from django import forms
from .models import Follower

class FollowerForm(forms.ModelForm):
    class Meta:
        model = Follower
        fields = ['telegram_id', 'name', 'note']  # Убрали 'date_of_exclusion'
