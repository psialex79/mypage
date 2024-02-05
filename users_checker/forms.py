from django import forms
from .models import Follower

class FollowerForm(forms.ModelForm):
    class Meta:
        model = Follower
        fields = ['telegram_id', 'date_of_exclusion', 'name', 'note']
